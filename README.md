# Word game helper

Little app to help you solve word games. Enter a list of letters, a length and it will output the list of words using these letters.

# Usage

## Command line

To run locally you need to install the following:
* `enchant`
* `aspell` and at least one dictionary (e.g. `aspell-en`)

```
Usage: words.py [OPTIONS]

  Run the solver from CLI.

Options:
  -L, --letters TEXT              Letters used in the word.  [required]
  -l, --length INTEGER            Length of the words to search.  [required]
  -d, --language TEXT             The language to search words (defaults to
                                  en_US)
  -c, --case-sensitive / --case-insensitive
                                  Should search be case sensitive (defaults to
                                  insensitive).
  --help                          Show this message and exit.
```

## Web

Run the following command then browse http://localhost:8000.

```
docker run -d -p 8000:8000 --name words nrouanet/words:latest
```

# Development

Install dev dependecies:
```
pipenv sync --dev
```

Run the development server with:
```
FLASK_APP=words.app FLASK_DEBUG=1 flask run
```
