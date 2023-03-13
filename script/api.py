from fastapi import FastAPI, Form

app = FastAPI()


@app.get("/")
async def read_file():
    f = open('../presentasjoner/files/text.txt', 'r')
    x = f.read()
    f.close()

    return {"message": x}

@app.put("/")
async def write_file(text: str | None = None):
    f = open('../presentasjoner/files/text.txt', 'a')
    f.write("\n"+text)
    f.close()

    return {"message": text + " written to file"}   