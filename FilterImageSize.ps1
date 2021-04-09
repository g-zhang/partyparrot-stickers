Add-Type -Assembly System.Drawing

function Get-Image
{
  process
  {
    $file = $_
    [Drawing.Image]::FromFile($_.FullName) | ForEach-Object {
      $_ | Add-Member -PassThru NoteProperty FullName ('{0}' -f $file.FullName)
    }
  }
}

$min = 128
Get-ChildItem -Path '.\apng\' -Filter *.png -Recurse | Get-Image | Where-Object { $_.Width -lt $min -or $_.Height -lt $min } | Select-Object -expa Fullname | Get-Item