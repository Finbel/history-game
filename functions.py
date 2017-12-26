import re


def get_event(event_string):
    regex = r'[JFMASDNO]{1}[anuryebchpilgstmov]{2,8} ([1-9]|[1-3][0-9]) \– (.*\n|.*)'
    returnstring = re.match(regex, event_string)
    if returnstring is not None:
        returnstring = returnstring.group(2)
    return returnstring


def parse_content(content):
    events = []
    parsing_events = False
    for line in content.split("\n"):
        line.strip()
        if "== Events ==" in line:
            parsing_events = True
            continue
        if ("==" in line) and (parsing_events) and ("===" not in line):
            parsing_events = False
            break
        if (parsing_events == True) and (len(line) > 15) and ("===" not in line):
            if not re.match(r'^[JFMASDNO]{1}[anuryebchpilgstmov]{2,8} ([1-9]|[1-3][0-9])?', line):
                events.append(line)
            else:
                event = get_event(line)
                if event is not None:
                    events.append(event)
    return events
