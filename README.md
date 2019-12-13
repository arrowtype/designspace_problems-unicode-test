# Unicodes test of DesignspaceProblems

https://github.com/LettError/DesignspaceProblems

https://github.com/LettError/DesignspaceProblems/issues/7

I wanted to check whether this code did what was intended, as I didn't quite understand it.

I've added some simple test UFOs plus a designspace in `unicodes-test-project`, and then made the script `build/lib/unicode-test.py` to check that designspace.

Sure enough, it's catching three different types of unicode issues:

- glyph of one name has unique unicodes between masters (i.e. /A has `0041` in one master, but `0080` in another
- glyph has "None" for its unicode value in some masters (i.e. /B has `0042` in one master, but `None` in another)
- glyph has two unicodes in one master, but just one unicode in another (i.e. /C has `0043` in one master, but `0043` _and_ `0049` in another)

```
▶ python designspace_problems-unicode-test.py

[[glyphs: different unicodes in glyph, glyphName: C unicodes: [73] (4, 10)],
[glyphs: different unicodes in glyph, glyphName: B unicodes: [None, 66] (4, 10)],
[glyphs: different unicodes in glyph, glyphName: A unicodes: [65, 128] (4, 10)]]
```

I made this test because I tend to interact with DesignspaceProblems via the DesignspaceEditor extension for RoboFont, and it doesn't (currently) catch these problems in the same designspace.

# Replicate test

1. Set up a venv: `python3 -m venv venv`
2. Activate it: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the test: `python designspace_problems-unicode-test.py`