# Cham Weather Forecast GUI

A small Tkinter desktop app that forecasts the weather in **Cham, Germany** using ARIMA time-series models.
Enter a date and the app shows predicted **temperature (°C)**, **relative humidity (%)**, **precipitation (mm/day)** and **wind speed (m/s)**.

## How it works

Each weather variable has its own model script (`arima_temp.py`, `arima_rh.py`, `arima_precp.py`, `arima_windspeed.py`):

1. Loads daily historical data from the matching CSV (from 2018 onward).
2. Runs an ADF stationarity test and `auto_arima` to explore the model order.
3. Fits an `ARIMA(1,0,1)` model, checks RMSE on the last 30 days, then refits on the full series.
4. Exposes a function that returns the forecast for a date in the 30-day window after the data ends
   (2021-12-30 to 2022-01-29).

`Final GUI.py` is the main app: it imports the four model modules and shows the predictions with icons.

## Project layout

| Path | Contents |
|---|---|
| `Final GUI.py` | Main Tkinter app (latest version) |
| `GUI.py`, `GUI Final.py`, `UI.py` | Earlier GUI iterations |
| `arima_*.py` | ARIMA model per weather variable |
| `*.csv` | Historical daily data for temperature, humidity, precipitation and wind speed |
| `icon/`, `*.png` | GUI icons and backgrounds |
| `Files/` | Packaged submission copy of the code, data and icons |
| `PRESENTATION 2.pptx` | Project presentation |

## Running it

```bash
pip install -r requirements.txt
python "Final GUI.py"
```

Enter a date as `YYYY-MM-DD` between 2021-12-30 and 2022-01-28 and click the search icon.

> **Note:** the scripts use absolute Windows paths (e.g. `D:/GUI/icon/...`, `D:\Temp data.csv`).
> Update these to match where you cloned the repo before running.
