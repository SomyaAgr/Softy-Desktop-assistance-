
import webbrowser

inp=input("enter topic you wannna search for: ")


def se(query):
    webbrowser.open_new_tab("https://en.wikipedia.org/wiki/"+query)

se(inp)

