import argparse
import json
import os

github_count = 0
package_count = 0


def json_parser(json_data):
    global github_count
    global package_count

    package_count += 1
    github_url_found = False

    try:
        url = json_data['info']['project_urls']['Homepage']
        if 'github.com' in url and not github_url_found:
            github_count += 1
            github_url_found = True
    except (TypeError, KeyError):
        pass

    try:
        url = json_data['info']['project_urls']['Source Code']
        if 'github.com' in url and not github_url_found:
            github_count += 1
            github_url_found = True
    except (TypeError, KeyError):
        pass

    try:
        url = json_data['info']['project_urls']['Download']
        if 'github.com' in url and not github_url_found:
            github_count += 1
            github_url_found = True
    except (TypeError, KeyError):
        pass

    try:
        url = json_data['info']['project_urls']['Bug Tracker']
        if 'github.com' in url and not github_url_found:
            github_count += 1
            github_url_found = True
    except (TypeError, KeyError):
        pass

    try:
        url = json_data['info']['home_page']
        if 'github.com' in url and not github_url_found:
            github_count += 1
            github_url_found = True
    except (TypeError, KeyError):
        pass

    try:
        url = json_data['info']['download_url']
        if 'github.com' in url and not github_url_found:
            github_count += 1
            github_url_found = True
    except (TypeError, KeyError):
        pass


def analyze(directory):
    # Open every file in the directory
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r') as f:
            json_data = json.load(f)
            json_parser(json_data)

    print("Package count:", package_count)
    print("Github repository count:", github_count, "(" + str(round(github_count / package_count * 100, 2)) + "%)")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', type=str)
    args = parser.parse_args()

    analyze(args.directory)


if __name__ == '__main__':
    main()
