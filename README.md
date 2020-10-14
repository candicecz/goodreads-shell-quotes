# Goodreads quote crawler

Script to crawl goodreads for literary quotes.

## Description

Creates a text file with quotes from a given quotes section (e.g. "literature", "philosophy") from goodreads.

I use this in tandem with `fortune` to generate quotes for my shell on startup.

## Getting Started

### To run script

Run the script to generate a quotes.txt file.

```
python3 script.py
```

### To generate a quote on startup

- Install fortune
  ```
  sudo apt-get install fortune
  ```
- Navigate to `/usr/games/` and create a data file(`.dat`) using your generated `quotes.txt` file
  ```
  strfile quotes.txt
  ```
- Run `fortune [filename]` to see a generated quote.
- If you want a quote to show up on terminal start update your `.bashrc` to check if the `.dat` file exists, then run the above `fortune` command.

```
# show a quote when terminal is open.
if [ -x /usr/games/fortune -a /usr/games/quotes.dat ]; then
  echo -e "\033[1;37m \n"; fortune /usr/games/quotes; echo -e "\n";
fi

```
