
# README
[中文](Readme_zh.md), [English](Readme_en.md)

---


# EasyReplace

EasyReplace is an image hosting source replacement tool designed to batch replace the CDN sources of image links in blog posts. When your CDN service is unavailable, simply run this tool to quickly replace the CDN source in all .md files within a specified folder. It also supports backup creation and reverting changes. With this tool, you can easily switch CDN acceleration services, ensuring that your blog content remains accessible in different network environments.

---

Blog Image Hosting Frequently Requires CDN Replacement

Sometimes, image hosting services for blogs may require changing the CDN in order for the images to be accessible from within China. This script is designed to solve this problem.

For example, the commonly used CDN https://cdn.jsdelivr.net may occasionally go down, requiring a replacement with http://fastly.jsdelivr.net or another CDN.

The script enumerates all .md files and replaces the image link prefixes with the new CDN.

Usage
	1.	View the manual

python EasyReplace.py -h
usage: EasyReplace.py [-h] -dir DIR -old OLD -new NEW [-clear] [-drawback]

e.g. python EasyReplace.py -dir "/Users/fxw/OneDrive/note" -old "https://cdn.jsdelivr.net" -new "http://fastly.jsdelivr.net"

options:
  -h, --help  show this help message and exit
  -dir DIR    The directory to change
  -old OLD    The old text to change
  -new NEW    The new text to change
  -clear      Clear all .back files
  -drawback   Restore all .back files

	2.	Replace image links: The program will enumerate all .md files, replace the image link prefixes with the new CDN, and generate a backup file with the .back extension.

For example:

python EasyReplace.py -dir "/Users/fxw/OneDrive/note" -old "https://cdn.jsdelivr.net" -new "http://fastlyjsdelivr.net"

	3.	(Optional) Revert changes by restoring the .back files:

python EasyReplace.py -dir "/Users/fxw/OneDrive/note" -old "https://cdn.jsdelivr.net" -new "http://fastlyjsdelivr.net" -drawback

	4.	(Optional) Delete the backup .back files:

python EasyReplace.py -dir "/Users/fxw/OneDrive/note" -old "https://cdn.jsdelivr.net" -new "http://fastlyjsdelivr.net" -clear