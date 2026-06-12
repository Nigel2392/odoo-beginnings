$parentDir = Split-Path -Parent $PSScriptRoot
$passwordPath = Join-Path $parentDir "odoo_pg_pass"
$password = (Get-Content -Path $passwordPath -Raw).Trim()

# 3. Execute the docker command using the variable
docker exec -it odoo odoo `
  -u ticketmaster `
  -d odoo-beginnings `
  --db_host=db `
  --db_user=odoo `
  --db_password=$password `
  --stop-after-init
