"""Jedes Notebook in einem frischen Kernel ausführen und Ausgaben speichern."""
from pathlib import Path
import os, sys, subprocess
ROOT = Path(__file__).resolve().parents[1]
from dotenv import load_dotenv
load_dotenv(ROOT / '.env', override=False)
if not os.getenv('BFH_API_KEY'):
    raise SystemExit('BFH_API_KEY fehlt. Zugang in .env oder als Umgebungsvariable eintragen.')
if len(sys.argv) == 1:
    # Alle Modellaufrufe verwenden die konfigurierte BFH-Schnittstelle.
    for path in sorted((ROOT/'notebooks').glob('*.ipynb')):
        env = dict(os.environ, MPLBACKEND='Agg', PYTHONIOENCODING='utf-8')
        subprocess.run([sys.executable,__file__,str(path)],check=True,env=env,cwd=ROOT)
else:
    import nbformat
    from nbclient import NotebookClient
    from jupyter_client.kernelspec import KernelSpecManager
    import tempfile,json
    path = Path(sys.argv[1])
    # Eigener Kernelspec verhindert die Wahl einer fremden Python-Installation.
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)/'projekt'; folder.mkdir()
        (folder/'kernel.json').write_text(json.dumps({'argv':[sys.executable,'-m','ipykernel_launcher','-f','{connection_file}'],
            'display_name':'Projekt','language':'python'}),encoding='utf-8')
        ksm = KernelSpecManager(kernel_dirs=[tmp])
        nb = nbformat.read(path,as_version=4)
        client = NotebookClient(nb,timeout=300,kernel_name='projekt',resources={'metadata':{'path':str(ROOT)}})
        client.km = __import__('jupyter_client').KernelManager(kernel_name='projekt',kernel_spec_manager=ksm)
        client.execute()
        nbformat.write(nb,path)
    print(path.name,'erfolgreich',flush=True)
