from pathlib import Path, PurePath
import soundfile as sf
import numpy
from typing import Optional

class InvalidSampleRate(Exception):
    """
    Thrown when supplied sample rate argument is invalid.
    """

class InvalidBitDepth(Exception):
    """
    Thrown when supplied bit depth argument is invalid.
    """

# class ConvertedFile:
#     def __init__(self, sample_rate: int, bit_depth: int, path: Optional[Path]=None)
#         self.sample_rate = sample_rate
#         self.bit


def get_audio_files(dir: Path, extensions: list[str]) -> list[Path]:
    files: list[Path] = [ item for item in dir.iterdir() if item.is_file() ]
    audio_files: list[Path] = [ file for file in files if file.suffix in extensions ] 
    return audio_files


def verify_dir(dir: Path):
    if not dir.exists():
        Path.mkdir(dir, parents=True)
        if dir.exists():
            print(f"{dir.as_posix()} exists!")


def convert_audio_files(files: list[Path], sr: int, bd: int, dst: Optional[Path]=None):
    if dst is not None:
        # write to dst
        for f in files:
            data, samplerate = sf.read(f)
            dst_file = dst.joinpath(f.name)
            # print(f"{f.name} will be written to {dst_file.as_posix()}")
            sf.write(dst_file, data, sr)
    else:
        # overwrite
        for f in files:
            with open(f, 'rw') as f:
                data, samplerate = sf.read(f)
                sf.write(f, data, sr)


def convert(src: Path, dst_sr: int, dst_bd: int, dst: Optional[Path]=None):
    EXTENSIONS = [
        ".wav",
        ".mp3",
        ".aiff",
    ]
    SAMPLE_RATES = [
        44100,
        48000,
    ]
    BIT_DEPTHS = [
        16,
        24
    ]

    # if `dst` is not supplied, just overwrite the files
    # if it is supplied, write the files to that location
    if dst is not None:
        verify_dir(dst)
        audio_files: list[Path] = get_audio_files(src, EXTENSIONS)
        try:
            convert_audio_files(audio_files, dst_sr, dst_bd, dst)
        except InvalidSampleRate:
            raise InvalidSampleRate(f"{dst_sr} is not valid!")
        except InvalidBitDepth:
            raise InvalidBitDepth(f"{dst_bd} is not valid!")
        # else:
            # no exceptions


def get_src(path: Optional[Path]=None) -> Path:
    if path is not None:
        return path
    else:
        new_path: Path = Path(input("Enter path of files to convert: "))
        try:
            new_path.resolve(strict=True)
        except FileNotFoundError as error:
            raise error
        else:
            return new_path


def get_dst(path: Optional[Path]=None) -> Path:
    if path is not None:
        return path
    else:
        new_path: Path = Path(input("Enter where to write converted files: "))
        try:
            new_path.resolve(strict=True)
        except FileNotFoundError as error:
            raise error
        else:
            return new_path


def main():
    DEV_SRC: Path = Path.home().joinpath("Desktop", "converter-of-the-drew", "files-to-convert", "_converted")
    DEV_DST: Path = DEV_SRC.joinpath("_converted")
    DEV_SR: int = 44100
    DEV_BD: int = 16

    src = get_src(DEV_SRC)
    dst = get_dst(DEV_DST)
    convert(src, DEV_SR, DEV_BD, dst)


if __name__ == "__main__":
    main()
