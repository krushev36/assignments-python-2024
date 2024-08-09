import operator

def sort_by_age(person):
    return person[2]

def person_lister(f):
    def inner(people):
        return [f(person) for person in sorted(people, key=sort_by_age)]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')