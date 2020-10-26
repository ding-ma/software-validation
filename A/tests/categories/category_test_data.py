url_category = "http://localhost:4567/categories"

category_create_json = {
    "title": "sometitle",
    "description": "some description"
}

category_create_xml = """<category>
  <description>t enim ad minim veni</description>
  <title>incididunt ut labora</title>
</category>
"""

category_create_xml_with_id = """<category>
  <active>true</active>
  <description>t enim ad minim veni</description>
  <title>incididunt ut labora</title>
</category>
"""

category_connect_task = """<todo>
  <id>1</id>
</todo>
"""