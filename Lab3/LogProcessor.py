import re


if __name__ == "__main__":

    pattern = r"\S+\s-\s-\s\[01/Jul/1995:(?:00:1\d\:\d{2}|00:20:00)\s\S+\]\s\"GET\s/\S+/NASA(?:\S+)\.gif\s\S+\"\s\d+\s\d+"
    number_of_matched_requests = 0
    read_lines = 0

    with open("access_log_Jul95") as file:
        for line in file:
            read_lines += 1
            if re.match(pattern, line):
                number_of_matched_requests += 1
                print(re.findall(pattern, line))

    print("\nNumber of all read lines: %d" % read_lines)
    print("\nNumber of all words NASA: %d" % number_of_matched_requests)
