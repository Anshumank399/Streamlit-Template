import re


def is_valid_datatype(datatype):
    print(datatype)
    valid_datatypes = [
        "int",
        "integer",
        "varchar",
        "text",
        "float",
        "double",
        "boolean",
        "date",
        "datetime",
    ]
    return datatype.lower() in valid_datatypes


def validate_dbml(check_string):
    # Remove leading and trailing whitespace
    dbml_string = check_string.strip()

    # Return False if the string is empty or contains only whitespace
    if not dbml_string or "Table" not in dbml_string:
        return False

    # Regular expression pattern for validating DBML file structure
    pattern = r"Table \w+ \{[^}]*\}"

    # Find all occurrences of the pattern in the DBML string
    matches = re.findall(pattern, dbml_string, re.DOTALL)

    # Check if the number of matches equals the number of tables
    if len(matches) != dbml_string.count("Table"):
        return False  # Valid DBML file
    else:
        return True


if __name__ == "__main__":
    print(validate_dbml(""))
    print(validate_dbml("Hello"))
    print(
        validate_dbml(
            """Table Users {
                        id int [pk]
                        name varchar
                        email varchar [unique]
                      }

                      Table Orders {
                        id int [pk]
                        user_id int [ref: > Users.id]
                        order_date datetime
                      }
                      """
        )
    )
    print(
        validate_dbml(
            "Table query_history { snowflake_query_id uuid database_id integer schema_id integer}"
        )
    )
