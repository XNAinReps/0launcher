import minecraft_launcher_lib as mclib
import subprocess


minecraft_directory = mclib.utils.get_minecraft_directory()
print("Bienvenido a 0launcher, Estas son las versiones instaladas: Si no encuentra la version deseada, ponla abajo")
forts = mclib.utils.get_installed_versions(minecraft_directory)

for fort in forts:
    print(fort["id"])


minecraft_version = input("¿Que version quieres usar?     > ")

mclib.install.install_minecraft_version(minecraft_version, minecraft_directory)
username = input("¿Que nick quieres usar?      > ")


options = {
    "username": username,
    "uuid": "",
    "token": "",

    "jvmArguments": ["-Xmx3G", "-Xms3G"],
    "launcher_version": "1.0 Alfa"
}

minecraft_command = mclib.command.get_minecraft_command(minecraft_version, minecraft_directory, options)
subprocess.run(minecraft_command)
quit
