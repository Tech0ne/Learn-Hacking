# Learn Hacking

---

Here are some dockers to learn some basics concepts of hacking

Please take notes of how to use it :

### Usage :

Choose the domain you want to learn (web, pwn...) and choose the lvl you want (see each dir).

Once you choose, please find the port using this logic :

The port is a 4 digits number where :
- First 2 are domain code (see the board below)
- Last 2 are given by the lvl nb (lvl 5 will be 05)


| Domain   | code |
|----------|------|
| web      | 10   |
| bin_exp  | 11   |
| forensic | 12   |
| cracking | 13   |
| pwn      | 14   |
| stegano  | 15   |

So, if you want to play the level 3 of pwn, the port will be 1403.

Once you got the port, you need to :

> Go to the directory you want to run
> Build the image with `docker build -t {image_name} .`
> And run it with `docker run -p {the_port}:{the_port} {image_name}`

Enjoy ;)
