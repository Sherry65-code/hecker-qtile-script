from os import system
from sys import exit

system("clear")

yon = print("Do you want to setup you internet connection ? (Y/n):")
if yon == "" or yon == "y" or yon == "Y":
    # Setup
    print("Setting up your intenet drivers...")
    system("""git clone https://aur.archlinux.org/rtw89-dkms-git.git
cd rtw89-dkms-git
makepkg -sri""")
    exit(0)
else:
    print("Ok continuing...")

print("Installing some basic packages...")
system("sudo pacman -S curl wget --noconfirm --needed")

print("Copying autostart script to home...")
system("cp ./.autostart.sh ~/")

print("Updating config file...")
system("cp ./config.py ~/.config/qtile/")

print("Installing necessary tools...")
system("yay -S picom nitrogen nm-applet xinput blueman bluez bluez-cups bluez-libs bluez-tools bluez-utils google-chrome jdk-openjdk brightnessctl nodejs npm discord telegram-desktop htop cmatrix neofetch visual-studio-code-bin ranger mesa vulkan-intel xf86-video-intel flatpak ln_sensors vim --needed")

print("Setting up the wallpapers...")
system("git clone https://github.com/D3Ext/aesthetic-wallpapers")

print("Setting up sound...")
system("sudo pacman -S sof-firmware pipewire pipewire-pulse wireplumber qpwgraph --noconfirm --needed")

print("Setting up bluetooth...")
system("sudo systemctl enable --now bluetooth.service")

print("Setting up vim...")
system("""curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim""")
system("git clone https://github.com/sherry65-code/hecker-vim")
system("cp ./hecker-vim/.vimrc ~/")
system("cp -r ./hecker-vim/.vim ~/")
system("rm -r hecker-vim")

print("Setting up python...")
system("sudo pacman -S python-pip --needed --noconfirm")

print("Installing creative tools...")
system("sudo pacman -S blender gimp --needed --noconfirm")

print("Installing python packages...")
system("sudo pacman -S python-psutil")

print("Installing fish...")
system("sudo pacman -S fish --needed --noconfirm")

print("Setting up fish...")
system("curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish")
system("omf install bobthefish")

print("Installing fonts...")
system("sudo pacman -S noto-fonts noto-fonts-emoji noto-fonts-extra --needed --noconfirm")

print("Installing management tools...")
system("")

print("Setting up gtk3 and xfce terminal...")
system("sudo pacman -S xfce4-terminal --needed --noconfirm")
system("""echo '@import 'colors.css';' \
    'VteTerminal, vte-terminal {' \
    'padding: 16px;' \
    '}' > ~/.config/gtk-3.0/gtk.css""")

print("Setup over")
print("ENJOY :)")
 
