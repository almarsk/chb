# Správa závislostí aplikace pomocí nástroje `poetry`

Pokyny k instalaci nástroje `poetry` jsou
[zde](https://python-poetry.org/docs/#installation), na stejných
stránkách je k dispozici i manuál, včetně [základního
přehledu](https://python-poetry.org/docs/basic-usage/). Klíčové příkazy
jsou nicméně vypsané níže.

```sh
# nápověda
$ poetry help

# instalace existujících závislostí definovaných v pyproject.toml /
# poetry.lock (např. při instalaci projektu na novém počítači, případně
# když je potřeba synchronizovat změny závislostí mezi počítači
$ poetry install

# přidání nové závislosti
$ poetry add ...

# otevření shellu s načteným prostředím se všemi závislostmi pro daný
# projekt
$ poetry shell

# v něm pak lze projekt spustit, ať už takto...
(in-project) $ python app.py

# ... či takto (což je trochu složitější, ale spolehlivější z hlediska
# restartu aplikace při změnách kódu)
(in-project) $ FLASK_ENV=development FLASK_APP=app flask run

# shell s prostředím projektu zase ukončíte pomocí příkazu exit či
# klávesovou zkratkou Ctrl+D
(in-project) $ exit

# příkazy lze v prostředí projektu spouštět i jednotlivě (tj. bez
# nutnosti nejdřív otevřít shell v prostředí projektu) pomocí příkazu
# `poetry run`
$ poetry run ...

# např. chceme-li spustit aplikaci, může to vypadat takto
$ FLASK_ENV=development FLASK_APP=app poetry run flask run
```
