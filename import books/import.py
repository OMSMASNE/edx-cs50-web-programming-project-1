# Copyright (C) 2019 OM SANTOSHKUMAR MASNE. All Rights Reserved.
# Licensed under the GNU Affero General Public License v3.0 only (AGPL-3.0-only) license.
# See License.txt in the project root for license information.

import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():
    file = open("books.csv")
    reader = csv.reader(file)
    next(reader)

    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
            {"isbn" : isbn, "title" : title, "author" : author, "year" : year})

        print(f"ADDED book with isbn: {isbn}, title: {title}, author: {author}, and year: {year}.")

    db.commit()

if __name__ == "__main__":
    main()
