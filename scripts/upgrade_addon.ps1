param(
    [string]$Mod="ticketmaster",
    [string]$Database="odoo-beginnings",
    [string]$PasswordFile="odoo_pg_pass"
)

# Retrieves the postgress password from the root project directory.
# Updates the ticketmaster(or other) module.
# https://www.odoo.com/documentation/19.0/developer/reference/cli.html#cmdoption-odoo-bin-u

$parentDir = Split-Path -Parent $PSScriptRoot
$passwordPath = Join-Path $parentDir $PasswordFile
$password = (Get-Content -Path $passwordPath -Raw).Trim()

docker exec -it odoo odoo `
  -u $Mod `
  -d $Database `
  --db_host=db `
  --db_user=odoo `
  --db_password=$password `
  --stop-after-init
