# Wakil Rakyat API

An unofficial REST API to access a list of wakil rakyats in the Malaysian parliament.

**IMPORTANT**: Please DON'T ABUSE the API, I'm running on free tier so bandwidth is limited. Just so that everyone can use it, please limit your usage, otherwise I'll have to block your IP, thanks!

## Endpoints

-   https://rrwz4p.deta.dev/kerusi/{kod} : returns an ahli parlimen according to it's kod parlimen
-   https://rrwz4p.deta.dev/kerusi : returns all ahli parlimen data
-   See https://rrwz4p.deta.dev/docs for more info

## TODOs

Add more endpoints, more data attributes etc. Feel free to suggest new features by [creating an issue](https://github.com/mujahidfa/wakil-rakyat-api/issues/new)!

## Project setup

### Install packages

```bash
pip install requirements-dev.txt
```

### Scrape latest data from [Portal Rasmi Parlimen Malaysia](https://www.parlimen.gov.my/)

```bash
python scrape.py
```

### Start the server

```bash
uvicorn main:app --reload
```

### Deploy to [Deta](https://www.deta.sh/)

```bash
# Need a Deta account
deta deploy
```
