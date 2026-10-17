#!/usr/bin/env python3
"""Zloží short 1080x1920 z fotiek/videí, titulkov a voliteľného zvuku (len ffmpeg, nič neplatí).

Použitie:
  python3 -I make_short.py --out short.mp4 --captions titulky.txt [--audio hlas.mp3] [--sec 2.5] zaber1.jpg zaber2.mp4 ...

titulky.txt – jeden titulok na riadok:  začiatok|koniec|text   (časy v sekundách, *slovo* = zvýraznené)
  0|1.8|Stačí *prísť*.
  1.8|3.2|Vstup *6 €*.
Fotky dostanú pomalý nájazd kamery, videá sa orežú na 9:16 a skrátia na --sec.
Bez --audio má video tichú stopu (YouTube aj TikTok ju vyžadujú pri pridaní hudby z ich knižnice).
"""
import argparse, os, re, subprocess, tempfile

W, H, FPS = 1080, 1920, 30
VIDEO_EXT = ('.mp4', '.mov', '.webm', '.mkv')


def ass_time(t):
    t = float(t)
    return '%d:%02d:%05.2f' % (t // 3600, t % 3600 // 60, t % 60)


def make_ass(path, font, accent):
    ev = []
    for line in open(path, encoding='utf-8'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        a, b, txt = line.split('|', 2)
        txt = re.sub(r'\*(.+?)\*', r'{\\c&H%s&}\1{\\c&HFFFFFF&}' % accent, txt)
        # krátky „pop“ pri každom titulku
        ev.append('Dialogue: 0,%s,%s,Cap,,0,0,0,,{\\fscx80\\fscy80\\t(0,120,\\fscx100\\fscy100)}%s'
                  % (ass_time(a), ass_time(b), txt))
    head = ('[Script Info]\nScriptType: v4.00+\nPlayResX: %d\nPlayResY: %d\nWrapStyle: 0\n\n'
            '[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, '
            'BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, '
            'Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n'
            # stred obrazovky, mimo prekrytia rozhrania YouTube (hore ~250 px, dole ~400 px)
            'Style: Cap,%s,112,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,7,3,5,90,90,0,1\n\n'
            '[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n'
            % (W, H, font))
    out = tempfile.NamedTemporaryFile('w', suffix='.ass', delete=False, encoding='utf-8')
    out.write(head + '\n'.join(ev) + '\n')
    out.close()
    return out.name


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--out', required=True)
    p.add_argument('--captions', required=True)
    p.add_argument('--audio')
    p.add_argument('--sec', type=float, default=2.5, help='dĺžka jedného záberu')
    p.add_argument('--font', default='Inter Display Black')
    p.add_argument('--accent', default='3FFFD4', help='farba zvýraznenia v BGR (3FFFD4 = limetková #D4FF3F)')
    p.add_argument('media', nargs='+')
    a = p.parse_args()

    ass = make_ass(a.captions, a.font, a.accent)
    frames = int(a.sec * FPS)
    cmd, parts = ['ffmpeg', '-y', '-hide_banner', '-loglevel', 'error'], []
    for i, m in enumerate(a.media):
        if m.lower().endswith(VIDEO_EXT):
            cmd += ['-t', str(a.sec), '-i', m]
            parts.append('[%d:v]scale=%d:%d:force_original_aspect_ratio=increase,crop=%d:%d,fps=%d,setsar=1,'
                         'trim=duration=%s,setpts=PTS-STARTPTS[v%d]' % (i, W, H, W, H, FPS, a.sec, i))
        else:
            # jedna snímka; zoompan z nej vyrobí presne `frames` snímok
            cmd += ['-i', m]
            zin = 'min(zoom+0.0009,1.12)' if i % 2 == 0 else 'if(eq(on,0),1.12,max(zoom-0.0009,1))'
            parts.append('[%d:v]scale=%d:%d:force_original_aspect_ratio=increase,crop=%d:%d,'
                         'zoompan=z=\'%s\':x=\'iw/2-iw/zoom/2\':y=\'ih/2-ih/zoom/2\':d=%d:s=%dx%d:fps=%d,'
                         'setsar=1[v%d]' % (i, W * 2, H * 2, W * 2, H * 2, zin, frames, W, H, FPS, i))
    n = len(a.media)
    total = n * a.sec
    esc = ass.replace('\\', '/').replace(':', '\\:')
    parts.append(''.join('[v%d]' % i for i in range(n)) + 'concat=n=%d:v=1:a=0,ass=\'%s\',format=yuv420p[v]' % (n, esc))
    if a.audio:
        cmd += ['-i', a.audio]
        amap = '%d:a' % n
    else:
        cmd += ['-f', 'lavfi', '-t', str(total), '-i', 'anullsrc=r=48000:cl=stereo']
        amap = '%d:a' % n
    cmd += ['-filter_complex', ';'.join(parts), '-map', '[v]', '-map', amap, '-t', str(total),
            '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-profile:v', 'high', '-r', str(FPS),
            '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', a.out]
    subprocess.run(cmd, check=True)
    os.unlink(ass)
    print('Hotovo: %s (%.1f s, %dx%d)' % (a.out, total, W, H))


if __name__ == '__main__':
    main()
