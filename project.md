## Web Framework

Prototyping: Streamlit

Production: TBC (Flask/NextJs/Svelte)

## Backend

When prototping can host on Streamlit. Later can host on Vercel/AWS/Others?

## Data Source

Lichess API: [https://lichess.org/api]

Chess.com API: [https://www.chess.com/news/view/published-data-api]

## Info to Show

When user enters username show following info:

- Basic Stat [Easy]
    - Performance against opponents of different ratings
    - Win/loss rate
    - Ratings progression
    - Losing method % (Resigns, Checkmates, etc.)
    - Info about different time controls
    - Histogram of game durations
- Advanced Stat [Hard]
    - Commonly played openings
    - Win rate for each opening + black/white
    - Allow users to add mutiple accounts and analyse as a whole
- Challenging [Impossible]
    - Heatmap to show where player plays around during diff parts of game
    - Play Style (Aggressive, Defensive, wtv)

We will add these features one by one.

## Database Info

Data to Store:
- Stats of popular players like Magnus and Hikaru (Demo)
- Openings Database

