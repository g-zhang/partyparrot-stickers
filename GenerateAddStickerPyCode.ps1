$path = ".\apng\"

Get-ChildItem -Path $path -Filter '*.png' | ForEach-Object { $("add_sticker(`"apng/{0}`", `"EMOJI`")" -f $_.Name) }