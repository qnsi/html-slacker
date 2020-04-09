from htmlslacker import HTMLSlacker


def test_example_1():
    html = """
    <b>Hello</b><br>
    There is <i>something</i> interesting about <code>this doc</code>

    <p>
    And <a href="http://example.com/">here is a
    link in a paragraph!</a>
    </p>
    """
    expected = "*Hello*\n There is _something_ interesting about `this doc` \n And <http://example.com/|here is a link in a paragraph!>"
    output = HTMLSlacker(html).get_output()
    assert(output == expected)


def test_style_not_rendered():
    html = '''<style><!-- /* stuff */ --></style>Dear Prudence'''
    expected = "Dear Prudence"
    output = HTMLSlacker(html).get_output()
    assert(output == expected)


def test_script_not_rendered():
    html = '''<script><!-- /* stuff */ --></script>Dear Prudence'''
    expected = "Dear Prudence"
    output = HTMLSlacker(html).get_output()
    assert(output == expected)


def test_link_with_target():
    html = 'Please click <a href="http://xxx.com/t.html" target="_blank">here</a>'
    expected = "Please click <http://xxx.com/t.html|here>"
    output = HTMLSlacker(html).get_output()
    assert(output == expected)

def test_pipedrive_test():
    # html = "Test <div><br></div><div>This is after newline</div><div><br></div><div><b><i><u>This is bold italic underlined</u></i></b></div><div><b><i><u><br></u></i></b></div><div><ul><li>this is unordered list</li><ul><li>nested</li></ul><li>unnested</li></ul><ol><li>ordered</li></ol></div>"
    html = "Test <div><br></div><div>This is after newline</div><div><br></div><div><b><i><u>This is bold italic underlined</u></i></b></div><div><b><i><u><br></u></i></b></div>"
    expected = "Test \nThis is after newline\n*_This is bold italic underlined_*"
    output = HTMLSlacker(html).get_output()
    assert(output == expected)
