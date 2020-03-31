# extract-list-item-texts-from-markdown


## What is this?

A tool to prepare text to put the questions into the slack custom response.
This extracts list sentences from a markdown file and outputs them to a text file.

Originally created for https://github.com/VGraupera/1on1-questions

To put the outputs into the slack custom response, search "random nuber of answers" here:

https://slackhq.com/mind-the-bot-a-guide-to-slackbot-custom-responses



## How to use

### Setup

Use pipenv

### Command

```bash
python main.py [input_markdown_file] > [output_text_file]
```
### Options

Edit target_heading in main.py to switch heading highlight