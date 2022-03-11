"""Test screencapture utility."""

import os
from datetime import datetime
from pathlib import Path
from unittest import TestCase
from unittest import main

from scriptbox.screencapture import Screenshot
from scriptbox.screencapture import ScreenshotNotification


class ScreenshotTestCase(TestCase):
    """Tests for Screenshot class."""

    def test_base_dir_finnish(self) -> None:
        path: str = str(Path.home()) + "/Kuvat/Näytönkaappaukset"
        self.assertEqual(Screenshot("fi_FI.UTF-8", "png")._base, path)

    def test_base_dir_english(self) -> None:
        path: str = str(Path.home()) + "/Pictures/Screenshots"
        self.assertEqual(Screenshot("en_US.UTF-8", "png")._base, path)

    def test_dst_dir_finnish(self) -> None:
        date: str = datetime.now().strftime("%d-%m-%Y, %A")
        home: str = str(Path.home())
        path: str = f"{home}/Kuvat/Näytönkaappaukset/{date}"
        self.assertEqual(Screenshot("fi_FI.UTF-8", "png")._dst, path)

    def test_dst_dir_english(self) -> None:
        date: str = datetime.now().strftime("%d-%m-%Y, %A")
        home: str = str(Path.home())
        path: str = f"{home}/Pictures/Screenshots/{date}"
        self.assertEqual(Screenshot("en_US.UTF-8", "png")._dst, path)

    def test_filename_finnish(self) -> None:
        date: str = datetime.now().strftime("%d-%m-%Y, %A")
        time: str = datetime.now().strftime("[%H:%M:%S]")
        home: str = str(Path.home())
        frmt: str = "png"
        name: str = f"{time} näytönkaappaus.{frmt}"
        path: str = f"{home}/Kuvat/Näytönkaappaukset/{date}/{name}"
        self.assertEqual(Screenshot("fi_FI.UTF-8", frmt)._name(), path)

    def test_filename_english(self) -> None:
        date: str = datetime.now().strftime("%d-%m-%Y, %A")
        time: str = datetime.now().strftime("[%H:%M:%S]")
        home: str = str(Path.home())
        frmt: str = "png"
        name: str = f"{time} screenshot.{frmt}"
        path: str = f"{home}/Pictures/Screenshots/{date}/{name}"
        self.assertEqual(Screenshot("en_US.UTF-8", frmt)._name(), path)

    def test_filename_id_finnish(self) -> None:
        id: str = Screenshot("fi_FI.UTF-8", "png")._id
        self.assertEqual(id, "näytönkaappaus")

    def test_filename_id_english(self) -> None:
        id: str = Screenshot("en_US.UTF-8", "png")._id
        self.assertEqual(id, "screenshot")


class ScreenshotNotificationTestCase(TestCase):
    """Tests for ScreenshotNotification class."""

    def test_subject_finnish(self) -> None:
        subject: str = ScreenshotNotification("fi_FI.UTF-8")._sub
        self.assertEqual(subject, "Näytönkaappaus")

    def test_subject_english(self) -> None:
        subject: str = ScreenshotNotification("en_US.UTF-8")._sub
        self.assertEqual(subject, "Screenshot")

    def test_body_finnish(self) -> None:
        body: str = ScreenshotNotification("fi_FI.UTF-8")._bdy
        self.assertEqual(body, "Näytönkaappaus otettu 📸 ")

    def test_body_english(self) -> None:
        body: str = ScreenshotNotification("en_US.UTF-8")._bdy
        self.assertEqual(body, "Screenshot taken 📸 ")


if __name__ == "__main__":
    main()
