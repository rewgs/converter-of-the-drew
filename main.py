from pathlib import Path, PurePath
import soundfile as sf
import numpy
from typing import Optional

from errors import InvalidBitDepth, InvalidSampleRate


def get_audio_files(dir: Path, extensions: list[str]) -> list[Path]:
    files: list[Path] = [ item for item in dir.iterdir() if item.is_file() ]
    audio_files: list[Path] = [ file for file in files if file.suffix in extensions ] 
    return audio_files


def verify_dir(dir: Path):
    if not dir.exists():
        Path.mkdir(dir, parents=True)
        if dir.exists():
            print(f"{dir.as_posix()} exists!")


class AudioFile:
    """
    Represents a new audio file created by this app.
    If destination directory is supplied, the original file is copied and converted with the specified settings.
    If no destination directory is supplied, the original file is overwritten with the specified settings.
    """
    def __init__(self, src: Path, sample_rate: int, bit_depth: int, dst: Optional[Path]=None):
        self.src: Path = src
        self.sample_rate = sample_rate
        self.bit_depth = bit_depth
        self.dst: Optional[Path] = dst

    def convert(self):
        """ Converts audio file. """

        def copy():
            """ Copies with new sample rate/bit depth/name to dst path. """

        def overwrite():
            """ Overwrites original audio file with new sample rate/bit depth/name. """

        if self.dst is not None:
            copy()
        else:
            overwrite()


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


def get_dir(prompt: str, path: Optional[Path]=None) -> Path:
    if path is not None:
        try:
            path.resolve(strict=True)
        except FileNotFoundError as error:
            raise error
        else:
            return path
    else:
        new_path: Path = Path(input(prompt))
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

    src = get_dir("Enter path of files to convert: " , DEV_DST)
    dst = get_dir("Enter where to write converted files: ", DEV_SRC)

    # convert(src, DEV_SR, DEV_BD, dst)


if __name__ == "__main__":
    main()
