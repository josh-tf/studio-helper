# studio-helper

A small Python script that logs in to a studio's Mindbody client portal so classes can be booked automatically.

> Archived. No longer maintained.

It starts Chrome inside a virtual (Xvfb) display, opens the studio's Mindbody page, signs in, then loads the "my schedule" page and prints the rows of the schedule table, saving a screenshot to `capture.png`. It was meant to run from cron or by hand. The booking step was never finished: the committed code stops after reading the schedule.

## Stack

- Python, Selenium 3 with ChromeDriver
- `pyvirtualdisplay` for running Chrome without a screen

## Develop

```sh
pip install "selenium<4" pyvirtualdisplay   # Selenium 3 API; also needs Chrome, ChromeDriver and Xvfb
export envStudio=... envUsername=... envPassword=...
python app.py
```

`envStudio` is the Mindbody studio ID; `envUsername` and `envPassword` are the portal login.

## License

[MIT](LICENSE)
