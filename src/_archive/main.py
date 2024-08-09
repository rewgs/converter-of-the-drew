from pathlib import Path, PurePath
import soundfile as sf


# def convert(dir: Path) -> :
#     EXTENSIONS = [
#         ".wav",
#         ".mp3",
#         ".aiff",
#     ]
#
#     for item in dir:
#         for ext in EXTENSIONS:
#             if d.suffix == ext:
#                 d_path = Path(PurePath(d).parent).resolve()
#                 new_name = f"{d.stem}_new.wav"
#                 new_file = PurePath.joinpath(d_path, new_name)
#                 subprocess.run(["sox", f"{d}", "-r", "44100", "-b", "16", f"{new_file}"])
#                 print(f"{d.stem} has been converted to {new_file.stem}")
#                 d.unlink() # deletes the old file
#                 new_file.rename(d) # renames the new file to the name of the old file
#             else:
#                 print(f"Skpping {d.name}, as it is not {ext}.")


def main():
    dir: Path = input("Enter directory contain files you want to convert: ")
    result = convert(dir: Path)


if __name__ == "__main__":
    main()
