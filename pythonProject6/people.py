"""
This is the people module and supports all the ReST actions for the
PEOPLE collection
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort
import os.path
import json


def read_file() -> dict:
    if not os.path.isfile("data.json"):
        with open("data.json", "w") as file:
            data = {}
            json.dump(data, file)
    else:
        with open("data.json") as file:
            data = json.load(file)
    return data


# Data to serve with our API


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        json string of list of people
    """
    return [read_file()]


def write_in_file(data: dict) -> None:
    try:
        with open("data.json", "w") as file:
            json.dump(data, file)
    except Exception as ex:
        abort(404, "Can't update or create in file. Error: ".format(ex))


def read_one(lname: str) -> dict:
    """
    This function responds to a request for /api/people/{lname}
    with one matching person from people

    :param lname:   last name of person to find
    :return:        person matching last name
    """
    # Does the person exist in people?
    data = read_file()
    if lname in data:
        person = data.get(lname)
        return person
    # otherwise, nope, not found
    else:
        abort(404, "Person with last name {lname} not found".format(lname=lname))


def create(person: dict) -> (dict, int):
    """
    This function creates a new person in the people structure
    based on the passed in person data

    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)
    position = person.get("position", None)
    projects = person.get("projects", None)
    skills = person.get("skills", None)

    # Does the person exist already?
    data = read_file()
    if lname not in data and lname is not None:
        data[lname] = {
            "fname": fname,
            "position": position,
            "projects": projects,
            "skills": skills,
        }
        write_in_file(data)
        return data[lname], 201

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Person with last name {lname} already exists".format(lname=lname),
        )


def update(lname: str, person: dict) -> dict:
    """
    This function updates an existing person in the people structure

    :param lname:   last name of person to update in the people structure
    :param person:  person to update
    :return:        updated person structure
    """
    # Does the person exist in people?
    data = read_file()
    if lname in data:
        data[lname]["fname"] = person.get("fname")
        data[lname]["position"] = person.get("position")
        data[lname]["projects"] = person.get("projects")
        data[lname]["skills"] = person.get("skills")

        write_in_file(data)
        return data[lname]

    # otherwise, nope, that's an error
    else:
        abort(404, "Person with last name {lname} not found".format(lname=lname))


def delete(lname):
    """
    This function deletes a person from the people structure

    :param lname:   last name of person to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the data to delete exist?
    data = read_file()
    if lname in data:
        del data[lname]
        write_in_file(data)
        return make_response("{lname} successfully deleted".format(lname=lname), 200)

    # Otherwise, nope, person to delete not found
    else:
        abort(404, "Person with last name {lname} not found".format(lname=lname))
