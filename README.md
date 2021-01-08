# Wakil Rakyat API

An unofficial REST API to access a list of wakil rakyats in the Malaysian parliament.

Data obtained from [Portal Data Terbuka Malaysia](https://www.data.gov.my/) and [DUN Sarawak](https://duns.sarawak.gov.my/page-0-40-150-Maklumat-Ahli-DUN-Sarawak.html).

**IMPORTANT**: Please DON'T ABUSE the API, I'm running on free tier so bandwidth is limited. Just so that everyone can use it, please limit your usage, otherwise I'll have to block your IP, thanks!

## Endpoints

-   `/parlimen` - returns all ahli parlimen data
-   `/parlimen/{kod_parlimen}` - returns an ahli parlimen data according to it's kod kerusi parlimen
-   `/parlimen/{kod_parlimen}/dun` - returns all DUN under a parlimen
-   `/parlimen/{kod_parlimen}/dun/{kod_dun}` - returns a DUN data under a parlimen according to it's kod kerusi DUN

See `/docs` for more info.

## TODOs

Add more endpoints, more data attributes etc. Feel free to suggest new features by [creating an issue](https://github.com/mujahidfa/wakil-rakyat-api/issues/new)!

## Project setup

### Install packages

```bash
pip install requirements-dev.txt
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
