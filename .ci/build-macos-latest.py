from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add(settings={"os.version": "10.13", "compiler.cppstd": "17"})
    builder.add(settings={"compiler.cppstd": "17"})
    builder.run()
