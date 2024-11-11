import os.path
import wave


def getPath(msg):
    file = msg + ".wav"
    if os.path.exists("do_z_stacji/" + file):
        return True, "do_z_stacji/" + file
    if os.path.exists("perony_i_tory/" + file):
        return True, "perony_i_tory/" + file
    if os.path.exists("stacje/" + file):
        return True, "stacje/" + file
    return False, ""


def findPaths(words):
    files = []
    current_word = ""
    for w in words:
        current_word += w
        var, path = getPath(current_word)
        # print(f"var: {var}, path: {path}, current_word: {current_word}")

        if not var:
            current_word += "_"
        elif var:
            current_word = ""
            files.append(path)
    return files


def generateWave(files):
    synthesis = "synthesis.wav"
    data = []
    for file in files:
        w = wave.open(file, 'rb')
        data.append([w.getparams(), w.readframes(w.getnframes())])
        w.close()

    output = wave.open(synthesis, 'wb')
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()


def __main__():
    prompt = input("Enter prompt to synthesis: ")
    # prompt = ("Pociag ze stacji Warszawa Wschodnia do stacji Poznan Glowny przez stacje Kutno, Konin odjedzie z toru "
    #           "drugiego przy peronie trzecim.")
    # prompt = ("Pociag do stacji Bialogard ze stacji Bydgoszcz Lesna przez stacje Babiak, Augustow, bedzin Miasto "
    #           "odjedzie z toru szostego przy peronie trzecim.")
    prompt = prompt.replace(".", "").replace(",", "").replace(":", "").lower()
    words = prompt.split(" ")
    files = findPaths(words)
    generateWave(files)


if __name__ == "__main__":
    __main__()
