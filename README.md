# The World Today — Saturday, 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/tataapri/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/tataapri/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A one-page newspaper poster summing up the world news of Saturday
21 November 2026, drawn programmatically with Pillow
(`draw_poster.py`, flat vector-style illustrations, no photos).
`main.ts` copies the finished `entry.png` to the output directory.
The image is 1024×1024 PNG, well under the 1 MiB limit, and two runs
of the program write byte-identical output.

## Stories

1. **Russian missiles land in Poland; NATO alerted** — Two Russian
   missiles and a suspected drone came down in Poland during a huge
   Russian attack on Ukraine. Warsaw calls it a deliberate provocation;
   NATO calls it a grave violation. Eight people were killed in
   Ukraine, and France seeks a UN Security Council meeting.
   Source: https://www.europesays.com/poland/38911/ (AP)
   and https://northlandnewsradio.com/2026/11/20/france-seeks-un-security-council-meeting-after-strikes-in-kyiv/ (Reuters)
2. **Wall Street plunges** — The S&P 500 slides into correction as the
   AI sell-off deepens; the Nasdaq falls 5.28% and Nvidia drops about
   14% after Friday's close, reported on 21 November.
   Source: https://oneturn.news/today/
3. **Denmark expels Russian envoy** — Copenhagen expels Russia's
   defence attaché over an alleged Russian-backed plot to kill
   Ukrainian rapper Kyivstoner at a concert near Copenhagen.
   Source: https://www.europesays.com/russia/92494/ (Al Jazeera)
4. **ANC scrambles for coalitions** — After its worst local-election
   result (31%), the ANC holds the most votes in only two of South
   Africa's eight big cities; parties have until 27 November to form
   local governments.
   Source: https://winnebanews.com/2026/11/21/anc-fights-to-keep-control-of-cities-after-election-setback/
5. **Mamdani: close Rikers by 2032** — New York City's mayor unveils
   the first comprehensive plan to close the Rikers Island jail, open
   four borough-based jails, and invest $146m in care and training.
   Source: https://criminaljustice.cityofnewyork.us/press-release/mayor-mamdani-releases-first-comprehensive-plan-to-close-rikers-island/
6. **Waymo recalls its robotaxis** — Alphabet's self-driving unit
   files two recalls after its cars entered closed freeway lanes and
   failed to follow manual traffic control.
   Source: https://947thebeast.com/2026/11/20/waymo-recalls-self-driving-cars-over-closed-freeway-lanes-manual-traffic-control/ (Reuters)
7. **Missiles over Riyadh stopped** — Saudi Arabia says it intercepted
   Houthi missiles over the capital, as its coalition strikes back.
   Source: https://oneturn.news/today/

All seven stories were reported on 21 November 2026 (events of the
night of 20–21 November and Friday's US developments as reported in
Saturday's editions). The poster names the day prominently in its
masthead: Saturday, 21 November 2026.

## Build

```sh
python3 draw_poster.py          # regenerates entry.png (1024x1024)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see LICENSE.
