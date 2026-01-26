2026-01-26T14:30:47.3923027Z Current runner version: '2.331.0'
2026-01-26T14:30:47.3958592Z ##[group]Runner Image Provisioner
2026-01-26T14:30:47.3960084Z Hosted Compute Agent
2026-01-26T14:30:47.3960935Z Version: 20260115.477
2026-01-26T14:30:47.3962058Z Commit: 4b342d620503cbe250a3154040964899ea7c9b00
2026-01-26T14:30:47.3963200Z Build Date: 2026-01-15T22:32:41Z
2026-01-26T14:30:47.3964272Z Worker ID: {3567f41c-d246-4b9d-9352-f940878681f4}
2026-01-26T14:30:47.3965465Z Azure Region: northcentralus
2026-01-26T14:30:47.3966421Z ##[endgroup]
2026-01-26T14:30:47.3968630Z ##[group]Operating System
2026-01-26T14:30:47.3969989Z Ubuntu
2026-01-26T14:30:47.3970877Z 24.04.3
2026-01-26T14:30:47.3971628Z LTS
2026-01-26T14:30:47.3972496Z ##[endgroup]
2026-01-26T14:30:47.3973300Z ##[group]Runner Image
2026-01-26T14:30:47.3974201Z Image: ubuntu-24.04
2026-01-26T14:30:47.3974989Z Version: 20260119.4.1
2026-01-26T14:30:47.3977226Z Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20260119.4/images/ubuntu/Ubuntu2404-Readme.md
2026-01-26T14:30:47.3980094Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20260119.4
2026-01-26T14:30:47.3981709Z ##[endgroup]
2026-01-26T14:30:47.3983669Z ##[group]GITHUB_TOKEN Permissions
2026-01-26T14:30:47.3986519Z Contents: read
2026-01-26T14:30:47.3987403Z Metadata: read
2026-01-26T14:30:47.3988178Z Packages: read
2026-01-26T14:30:47.3989522Z ##[endgroup]
2026-01-26T14:30:47.3992878Z Secret source: Actions
2026-01-26T14:30:47.3994009Z Prepare workflow directory
2026-01-26T14:30:47.4731148Z Prepare all required actions
2026-01-26T14:30:47.4851704Z Getting action download info
2026-01-26T14:30:47.9243954Z Download action repository 'actions/checkout@v4' (SHA:34e114876b0b11c390a56381ad16ebd13914f8d5)
2026-01-26T14:30:48.0443721Z Download action repository 'actions/setup-python@v5' (SHA:a26af69be951a213d495a4c3e4e4022e16d87065)
2026-01-26T14:30:48.1383014Z Download action repository 'actions/cache@v3' (SHA:6f8efc29b200d32929f49075959781ed54ec270c)
2026-01-26T14:30:48.6253429Z Complete job name: test (3.10)
2026-01-26T14:30:48.7058146Z ##[group]Run actions/checkout@v4
2026-01-26T14:30:48.7059676Z with:
2026-01-26T14:30:48.7060393Z   repository: Nik0lay1/ProjectMindMCP
2026-01-26T14:30:48.7061672Z   token: ***
2026-01-26T14:30:48.7062378Z   ssh-strict: true
2026-01-26T14:30:48.7063054Z   ssh-user: git
2026-01-26T14:30:48.7063744Z   persist-credentials: true
2026-01-26T14:30:48.7064533Z   clean: true
2026-01-26T14:30:48.7065235Z   sparse-checkout-cone-mode: true
2026-01-26T14:30:48.7066124Z   fetch-depth: 1
2026-01-26T14:30:48.7066821Z   fetch-tags: false
2026-01-26T14:30:48.7067537Z   show-progress: true
2026-01-26T14:30:48.7068251Z   lfs: false
2026-01-26T14:30:48.7069058Z   submodules: false
2026-01-26T14:30:48.7069807Z   set-safe-directory: true
2026-01-26T14:30:48.7070893Z ##[endgroup]
2026-01-26T14:30:48.8297413Z Syncing repository: Nik0lay1/ProjectMindMCP
2026-01-26T14:30:48.8303996Z ##[group]Getting Git version info
2026-01-26T14:30:48.8307551Z Working directory is '/home/runner/work/ProjectMindMCP/ProjectMindMCP'
2026-01-26T14:30:48.8310575Z [command]/usr/bin/git version
2026-01-26T14:30:48.8379791Z git version 2.52.0
2026-01-26T14:30:48.8413025Z ##[endgroup]
2026-01-26T14:30:48.8429229Z Temporarily overriding HOME='/home/runner/work/_temp/c2188752-e41f-4a46-8c71-34f154a62df7' before making global git config changes
2026-01-26T14:30:48.8434941Z Adding repository directory to the temporary git global config as a safe directory
2026-01-26T14:30:48.8452700Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/ProjectMindMCP/ProjectMindMCP
2026-01-26T14:30:48.8503231Z Deleting the contents of '/home/runner/work/ProjectMindMCP/ProjectMindMCP'
2026-01-26T14:30:48.8509481Z ##[group]Initializing the repository
2026-01-26T14:30:48.8514447Z [command]/usr/bin/git init /home/runner/work/ProjectMindMCP/ProjectMindMCP
2026-01-26T14:30:48.8625048Z hint: Using 'master' as the name for the initial branch. This default branch name
2026-01-26T14:30:48.8628572Z hint: will change to "main" in Git 3.0. To configure the initial branch name
2026-01-26T14:30:48.8633906Z hint: to use in all of your new repositories, which will suppress this warning,
2026-01-26T14:30:48.8636794Z hint: call:
2026-01-26T14:30:48.8637828Z hint:
2026-01-26T14:30:48.8639412Z hint: 	git config --global init.defaultBranch <name>
2026-01-26T14:30:48.8641653Z hint:
2026-01-26T14:30:48.8643744Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2026-01-26T14:30:48.8646710Z hint: 'development'. The just-created branch can be renamed via this command:
2026-01-26T14:30:48.8649110Z hint:
2026-01-26T14:30:48.8650168Z hint: 	git branch -m <name>
2026-01-26T14:30:48.8651465Z hint:
2026-01-26T14:30:48.8653137Z hint: Disable this message with "git config set advice.defaultBranchName false"
2026-01-26T14:30:48.8656449Z Initialized empty Git repository in /home/runner/work/ProjectMindMCP/ProjectMindMCP/.git/
2026-01-26T14:30:48.8663065Z [command]/usr/bin/git remote add origin https://github.com/Nik0lay1/ProjectMindMCP
2026-01-26T14:30:48.8690995Z ##[endgroup]
2026-01-26T14:30:48.8693729Z ##[group]Disabling automatic garbage collection
2026-01-26T14:30:48.8695882Z [command]/usr/bin/git config --local gc.auto 0
2026-01-26T14:30:48.8730271Z ##[endgroup]
2026-01-26T14:30:48.8732305Z ##[group]Setting up auth
2026-01-26T14:30:48.8737606Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-01-26T14:30:48.8775529Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-01-26T14:30:48.9157147Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-01-26T14:30:48.9197874Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-01-26T14:30:48.9445857Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-01-26T14:30:48.9486534Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-01-26T14:30:48.9806683Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2026-01-26T14:30:48.9817819Z ##[endgroup]
2026-01-26T14:30:48.9820402Z ##[group]Fetching the repository
2026-01-26T14:30:48.9828194Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +22f1d8160a4b10a110d9de8158338743ddb56e25:refs/remotes/origin/main
2026-01-26T14:30:49.2990969Z From https://github.com/Nik0lay1/ProjectMindMCP
2026-01-26T14:30:49.2991932Z  * [new ref]         22f1d8160a4b10a110d9de8158338743ddb56e25 -> origin/main
2026-01-26T14:30:49.3019456Z ##[endgroup]
2026-01-26T14:30:49.3022240Z ##[group]Determining the checkout info
2026-01-26T14:30:49.3025247Z ##[endgroup]
2026-01-26T14:30:49.3027873Z [command]/usr/bin/git sparse-checkout disable
2026-01-26T14:30:49.3071217Z [command]/usr/bin/git config --local --unset-all extensions.worktreeConfig
2026-01-26T14:30:49.3101235Z ##[group]Checking out the ref
2026-01-26T14:30:49.3105083Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
2026-01-26T14:30:49.3193679Z Switched to a new branch 'main'
2026-01-26T14:30:49.3197633Z branch 'main' set up to track 'origin/main'.
2026-01-26T14:30:49.3207165Z ##[endgroup]
2026-01-26T14:30:49.3247311Z [command]/usr/bin/git log -1 --format=%H
2026-01-26T14:30:49.3272138Z 22f1d8160a4b10a110d9de8158338743ddb56e25
2026-01-26T14:30:49.3541616Z ##[group]Run actions/setup-python@v5
2026-01-26T14:30:49.3542380Z with:
2026-01-26T14:30:49.3542986Z   python-version: 3.10
2026-01-26T14:30:49.3543688Z   check-latest: false
2026-01-26T14:30:49.3544598Z   token: ***
2026-01-26T14:30:49.3545008Z   update-environment: true
2026-01-26T14:30:49.3545450Z   allow-prereleases: false
2026-01-26T14:30:49.3546305Z   freethreaded: false
2026-01-26T14:30:49.3546681Z ##[endgroup]
2026-01-26T14:30:49.5746657Z ##[group]Installed versions
2026-01-26T14:30:49.5762794Z Successfully set up CPython (3.10.19)
2026-01-26T14:30:49.5763854Z ##[endgroup]
2026-01-26T14:30:49.7113975Z ##[group]Run actions/cache@v3
2026-01-26T14:30:49.7114436Z with:
2026-01-26T14:30:49.7114755Z   path: ~/.cache/pip
2026-01-26T14:30:49.7115282Z   key: Linux-pip-dc256607d04067962fd327583382ffc58d841f2f713bc2a7de34a949b022636d
2026-01-26T14:30:49.7115876Z   restore-keys: Linux-pip-

2026-01-26T14:30:49.7116270Z   enableCrossOsArchive: false
2026-01-26T14:30:49.7116668Z   fail-on-cache-miss: false
2026-01-26T14:30:49.7117030Z   lookup-only: false
2026-01-26T14:30:49.7117359Z env:
2026-01-26T14:30:49.7117743Z   pythonLocation: /opt/hostedtoolcache/Python/3.10.19/x64
2026-01-26T14:30:49.7118371Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.10.19/x64/lib/pkgconfig
2026-01-26T14:30:49.7119340Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.10.19/x64
2026-01-26T14:30:49.7119935Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.10.19/x64
2026-01-26T14:30:49.7120488Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.10.19/x64
2026-01-26T14:30:49.7121081Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.10.19/x64/lib
2026-01-26T14:30:49.7121549Z ##[endgroup]
2026-01-26T14:30:50.0125807Z Cache not found for input keys: Linux-pip-dc256607d04067962fd327583382ffc58d841f2f713bc2a7de34a949b022636d, Linux-pip-
2026-01-26T14:30:50.0233211Z ##[group]Run python -m pip install --upgrade pip
2026-01-26T14:30:50.0233855Z [36;1mpython -m pip install --upgrade pip[0m
2026-01-26T14:30:50.0234330Z [36;1mpip install -e ".[dev]"[0m
2026-01-26T14:30:50.0277454Z shell: /usr/bin/bash -e {0}
2026-01-26T14:30:50.0277863Z env:
2026-01-26T14:30:50.0278286Z   pythonLocation: /opt/hostedtoolcache/Python/3.10.19/x64
2026-01-26T14:30:50.0279215Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.10.19/x64/lib/pkgconfig
2026-01-26T14:30:50.0279820Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.10.19/x64
2026-01-26T14:30:50.0280395Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.10.19/x64
2026-01-26T14:30:50.0280954Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.10.19/x64
2026-01-26T14:30:50.0281524Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.10.19/x64/lib
2026-01-26T14:30:50.0281999Z ##[endgroup]
2026-01-26T14:30:50.9124863Z Requirement already satisfied: pip in /opt/hostedtoolcache/Python/3.10.19/x64/lib/python3.10/site-packages (25.3)
2026-01-26T14:30:51.6871849Z Obtaining file:///home/runner/work/ProjectMindMCP/ProjectMindMCP
2026-01-26T14:30:51.6889796Z   Installing build dependencies: started
2026-01-26T14:30:52.7379913Z   Installing build dependencies: finished with status 'done'
2026-01-26T14:30:52.7399647Z   Checking if build backend supports build_editable: started
2026-01-26T14:30:53.1303176Z   Checking if build backend supports build_editable: finished with status 'done'
2026-01-26T14:30:53.1313995Z   Getting requirements to build editable: started
2026-01-26T14:30:53.4540079Z   Getting requirements to build editable: finished with status 'done'
2026-01-26T14:30:53.4552849Z   Preparing editable metadata (pyproject.toml): started
2026-01-26T14:30:53.6371345Z   Preparing editable metadata (pyproject.toml): finished with status 'done'
2026-01-26T14:30:53.7289851Z Collecting mcp>=0.1.0 (from projectmind==0.4.0)
2026-01-26T14:30:53.7816169Z   Downloading mcp-1.26.0-py3-none-any.whl.metadata (89 kB)
2026-01-26T14:30:53.8815857Z Collecting chromadb>=0.4.0 (from projectmind==0.4.0)
2026-01-26T14:30:53.8851620Z   Downloading chromadb-1.4.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.2 kB)
2026-01-26T14:30:53.9089776Z Collecting sentence-transformers>=2.2.0 (from projectmind==0.4.0)
2026-01-26T14:30:53.9141709Z   Downloading sentence_transformers-5.2.0-py3-none-any.whl.metadata (16 kB)
2026-01-26T14:30:53.9331970Z Collecting langchain-text-splitters>=0.0.1 (from projectmind==0.4.0)
2026-01-26T14:30:53.9380131Z   Downloading langchain_text_splitters-1.1.0-py3-none-any.whl.metadata (2.7 kB)
2026-01-26T14:30:53.9663250Z Collecting GitPython>=3.1.0 (from projectmind==0.4.0)
2026-01-26T14:30:53.9696572Z   Downloading gitpython-3.1.46-py3-none-any.whl.metadata (13 kB)
2026-01-26T14:30:53.9934940Z Collecting radon>=6.0.0 (from projectmind==0.4.0)
2026-01-26T14:30:53.9984683Z   Downloading radon-6.0.1-py2.py3-none-any.whl.metadata (8.2 kB)
2026-01-26T14:30:54.0438064Z Collecting pylint>=3.0.0 (from projectmind==0.4.0)
2026-01-26T14:30:54.0483023Z   Downloading pylint-4.0.4-py3-none-any.whl.metadata (12 kB)
2026-01-26T14:30:54.0955110Z Collecting pytest>=7.0.0 (from projectmind==0.4.0)
2026-01-26T14:30:54.1003649Z   Downloading pytest-9.0.2-py3-none-any.whl.metadata (7.6 kB)
2026-01-26T14:30:54.1247331Z Collecting pytest-cov>=4.0.0 (from projectmind==0.4.0)
2026-01-26T14:30:54.1286024Z   Downloading pytest_cov-7.0.0-py3-none-any.whl.metadata (31 kB)
2026-01-26T14:30:54.1945727Z Collecting black>=23.0.0 (from projectmind==0.4.0)
2026-01-26T14:30:54.1990687Z   Downloading black-26.1.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (88 kB)
2026-01-26T14:30:54.6813028Z Collecting ruff>=0.1.0 (from projectmind==0.4.0)
2026-01-26T14:30:54.6861138Z   Downloading ruff-0.14.14-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (26 kB)
2026-01-26T14:30:54.8173450Z Collecting mypy>=1.0.0 (from projectmind==0.4.0)
2026-01-26T14:30:54.8229456Z   Downloading mypy-1.19.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.2 kB)
2026-01-26T14:30:54.8694976Z Collecting pre-commit>=3.0.0 (from projectmind==0.4.0)
2026-01-26T14:30:54.8729739Z   Downloading pre_commit-4.5.1-py2.py3-none-any.whl.metadata (1.2 kB)
2026-01-26T14:30:54.8946474Z Collecting click>=8.0.0 (from black>=23.0.0->projectmind==0.4.0)
2026-01-26T14:30:54.8980020Z   Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
2026-01-26T14:30:54.9091805Z Collecting mypy-extensions>=0.4.3 (from black>=23.0.0->projectmind==0.4.0)
2026-01-26T14:30:54.9124681Z   Downloading mypy_extensions-1.1.0-py3-none-any.whl.metadata (1.1 kB)
2026-01-26T14:30:54.9305861Z Collecting packaging>=22.0 (from black>=23.0.0->projectmind==0.4.0)
2026-01-26T14:30:54.9320645Z   Using cached packaging-26.0-py3-none-any.whl.metadata (3.3 kB)
2026-01-26T14:30:54.9457664Z Collecting pathspec>=1.0.0 (from black>=23.0.0->projectmind==0.4.0)
2026-01-26T14:30:54.9489920Z   Downloading pathspec-1.0.3-py3-none-any.whl.metadata (13 kB)
2026-01-26T14:30:54.9726666Z Collecting platformdirs>=2 (from black>=23.0.0->projectmind==0.4.0)
2026-01-26T14:30:54.9765769Z   Downloading platformdirs-4.5.1-py3-none-any.whl.metadata (12 kB)
2026-01-26T14:30:54.9946611Z Collecting pytokens>=0.3.0 (from black>=23.0.0->projectmind==0.4.0)
2026-01-26T14:30:54.9998515Z   Downloading pytokens-0.4.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (3.8 kB)
2026-01-26T14:30:55.0239284Z Collecting tomli>=1.1.0 (from black>=23.0.0->projectmind==0.4.0)
2026-01-26T14:30:55.0275527Z   Downloading tomli-2.4.0-py3-none-any.whl.metadata (10 kB)
2026-01-26T14:30:55.0500308Z Collecting typing-extensions>=4.0.1 (from black>=23.0.0->projectmind==0.4.0)
2026-01-26T14:30:55.0543661Z   Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
2026-01-26T14:30:55.0714850Z Collecting build>=1.0.3 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:55.0750912Z   Downloading build-1.4.0-py3-none-any.whl.metadata (5.8 kB)
2026-01-26T14:30:55.2586990Z Collecting pydantic>=1.9 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:55.2624766Z   Downloading pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
2026-01-26T14:30:55.3929919Z Collecting pybase64>=1.4.1 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:55.4005853Z   Downloading pybase64-1.4.3-cp310-cp310-manylinux1_x86_64.manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_5_x86_64.whl.metadata (8.7 kB)
2026-01-26T14:30:55.4345757Z Collecting uvicorn>=0.18.3 (from uvicorn[standard]>=0.18.3->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:55.4381800Z   Downloading uvicorn-0.40.0-py3-none-any.whl.metadata (6.7 kB)
2026-01-26T14:30:55.6813482Z Collecting numpy>=1.22.5 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:55.6849880Z   Downloading numpy-2.2.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (62 kB)
2026-01-26T14:30:55.7356774Z Collecting posthog<6.0.0,>=2.4.0 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:55.7403606Z   Downloading posthog-5.4.0-py3-none-any.whl.metadata (5.7 kB)
2026-01-26T14:30:55.8228173Z Collecting onnxruntime>=1.14.1 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:55.8283380Z   Downloading onnxruntime-1.23.2-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (5.1 kB)
2026-01-26T14:30:55.8998584Z Collecting opentelemetry-api>=1.2.0 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:55.9035806Z   Downloading opentelemetry_api-1.39.1-py3-none-any.whl.metadata (1.5 kB)
2026-01-26T14:30:55.9274011Z Collecting opentelemetry-exporter-otlp-proto-grpc>=1.2.0 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:55.9308742Z   Downloading opentelemetry_exporter_otlp_proto_grpc-1.39.1-py3-none-any.whl.metadata (2.5 kB)
2026-01-26T14:30:55.9575776Z Collecting opentelemetry-sdk>=1.2.0 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:55.9608634Z   Downloading opentelemetry_sdk-1.39.1-py3-none-any.whl.metadata (1.5 kB)
2026-01-26T14:30:56.1494126Z Collecting tokenizers>=0.13.2 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:56.1531617Z   Downloading tokenizers-0.22.2-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
2026-01-26T14:30:56.1823503Z Collecting pypika>=0.48.9 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:56.1864312Z   Downloading pypika-0.50.0-py2.py3-none-any.whl.metadata (51 kB)
2026-01-26T14:30:56.2250432Z Collecting tqdm>=4.65.0 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:56.2292638Z   Downloading tqdm-4.67.1-py3-none-any.whl.metadata (57 kB)
2026-01-26T14:30:56.2530289Z Collecting overrides>=7.3.1 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:56.2553486Z   Downloading overrides-7.7.0-py3-none-any.whl.metadata (5.8 kB)
2026-01-26T14:30:56.2818689Z Collecting importlib-resources (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:56.2856992Z   Downloading importlib_resources-6.5.2-py3-none-any.whl.metadata (3.9 kB)
2026-01-26T14:30:56.9662823Z Collecting grpcio>=1.58.0 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:56.9701904Z   Downloading grpcio-1.76.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (3.7 kB)
2026-01-26T14:30:57.0204424Z Collecting bcrypt>=4.0.1 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:57.0241614Z   Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl.metadata (10 kB)
2026-01-26T14:30:57.0487802Z Collecting typer>=0.9.0 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:57.0522606Z   Downloading typer-0.21.1-py3-none-any.whl.metadata (16 kB)
2026-01-26T14:30:57.0827118Z Collecting kubernetes>=28.1.0 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:57.0865148Z   Downloading kubernetes-35.0.0-py2.py3-none-any.whl.metadata (1.7 kB)
2026-01-26T14:30:57.1118000Z Collecting tenacity>=8.2.3 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:57.1153538Z   Downloading tenacity-9.1.2-py3-none-any.whl.metadata (1.2 kB)
2026-01-26T14:30:57.1628026Z Collecting pyyaml>=6.0.0 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:57.1664494Z   Downloading pyyaml-6.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
2026-01-26T14:30:57.2897190Z Collecting mmh3>=4.0.1 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:57.2934629Z   Downloading mmh3-5.2.0-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (14 kB)
2026-01-26T14:30:57.6096224Z Collecting orjson>=3.9.12 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:57.6133551Z   Downloading orjson-3.11.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (41 kB)
2026-01-26T14:30:57.6373771Z Collecting httpx>=0.27.0 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:57.6413276Z   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
2026-01-26T14:30:57.6912495Z Collecting rich>=10.11.0 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:57.6976691Z   Downloading rich-14.3.1-py3-none-any.whl.metadata (18 kB)
2026-01-26T14:30:57.7275136Z Collecting jsonschema>=4.19.0 (from chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:57.7315896Z   Downloading jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
2026-01-26T14:30:57.7712511Z Collecting requests<3.0,>=2.7 (from posthog<6.0.0,>=2.4.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:57.7750072Z   Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
2026-01-26T14:30:57.7919198Z Collecting six>=1.5 (from posthog<6.0.0,>=2.4.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:57.7955875Z   Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
2026-01-26T14:30:57.8115300Z Collecting python-dateutil>=2.2 (from posthog<6.0.0,>=2.4.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:57.8150760Z   Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
2026-01-26T14:30:57.8326590Z Collecting backoff>=1.10.0 (from posthog<6.0.0,>=2.4.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:57.8360668Z   Downloading backoff-2.2.1-py3-none-any.whl.metadata (14 kB)
2026-01-26T14:30:57.8496444Z Collecting distro>=1.5.0 (from posthog<6.0.0,>=2.4.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:57.8530063Z   Downloading distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
2026-01-26T14:30:57.9567471Z Collecting charset_normalizer<4,>=2 (from requests<3.0,>=2.7->posthog<6.0.0,>=2.4.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:57.9609691Z   Downloading charset_normalizer-3.4.4-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (37 kB)
2026-01-26T14:30:57.9783700Z Collecting idna<4,>=2.5 (from requests<3.0,>=2.7->posthog<6.0.0,>=2.4.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:57.9827784Z   Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
2026-01-26T14:30:58.0169989Z Collecting urllib3<3,>=1.21.1 (from requests<3.0,>=2.7->posthog<6.0.0,>=2.4.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:58.0207706Z   Downloading urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
2026-01-26T14:30:58.0476466Z Collecting certifi>=2017.4.17 (from requests<3.0,>=2.7->posthog<6.0.0,>=2.4.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:58.0511154Z   Downloading certifi-2026.1.4-py3-none-any.whl.metadata (2.5 kB)
2026-01-26T14:30:58.0728535Z Collecting pyproject_hooks (from build>=1.0.3->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:58.0761179Z   Downloading pyproject_hooks-1.2.0-py3-none-any.whl.metadata (1.3 kB)
2026-01-26T14:30:58.0945844Z Collecting gitdb<5,>=4.0.1 (from GitPython>=3.1.0->projectmind==0.4.0)
2026-01-26T14:30:58.0980860Z   Downloading gitdb-4.0.12-py3-none-any.whl.metadata (1.2 kB)
2026-01-26T14:30:58.1128252Z Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->GitPython>=3.1.0->projectmind==0.4.0)
2026-01-26T14:30:58.1161170Z   Downloading smmap-5.0.2-py3-none-any.whl.metadata (4.3 kB)
2026-01-26T14:30:58.1501305Z Collecting anyio (from httpx>=0.27.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:58.1537561Z   Downloading anyio-4.12.1-py3-none-any.whl.metadata (4.3 kB)
2026-01-26T14:30:58.1777392Z Collecting httpcore==1.* (from httpx>=0.27.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:58.1811486Z   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
2026-01-26T14:30:58.1984276Z Collecting h11>=0.16 (from httpcore==1.*->httpx>=0.27.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:58.2020474Z   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
2026-01-26T14:30:58.2212985Z Collecting attrs>=22.2.0 (from jsonschema>=4.19.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:58.2246637Z   Downloading attrs-25.4.0-py3-none-any.whl.metadata (10 kB)
2026-01-26T14:30:58.2401729Z Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=4.19.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:58.2433325Z   Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
2026-01-26T14:30:58.2729161Z Collecting referencing>=0.28.4 (from jsonschema>=4.19.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:58.2765410Z   Downloading referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
2026-01-26T14:30:58.6996029Z Collecting rpds-py>=0.25.0 (from jsonschema>=4.19.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:58.7036408Z   Downloading rpds_py-0.30.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB)
2026-01-26T14:30:58.7695506Z Collecting websocket-client!=0.40.0,!=0.41.*,!=0.42.*,>=0.32.0 (from kubernetes>=28.1.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:58.7734499Z   Downloading websocket_client-1.9.0-py3-none-any.whl.metadata (8.3 kB)
2026-01-26T14:30:58.7900960Z Collecting requests-oauthlib (from kubernetes>=28.1.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:58.7938263Z   Downloading requests_oauthlib-2.0.0-py2.py3-none-any.whl.metadata (11 kB)
2026-01-26T14:30:58.8249165Z Collecting durationpy>=0.7 (from kubernetes>=28.1.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:58.8285947Z   Downloading durationpy-0.10-py3-none-any.whl.metadata (340 bytes)
2026-01-26T14:30:58.8943754Z Collecting langchain-core<2.0.0,>=1.2.0 (from langchain-text-splitters>=0.0.1->projectmind==0.4.0)
2026-01-26T14:30:58.8990030Z   Downloading langchain_core-1.2.7-py3-none-any.whl.metadata (3.7 kB)
2026-01-26T14:30:58.9192991Z Collecting jsonpatch<2.0.0,>=1.33.0 (from langchain-core<2.0.0,>=1.2.0->langchain-text-splitters>=0.0.1->projectmind==0.4.0)
2026-01-26T14:30:58.9231084Z   Downloading jsonpatch-1.33-py2.py3-none-any.whl.metadata (3.0 kB)
2026-01-26T14:30:59.0096652Z Collecting langsmith<1.0.0,>=0.3.45 (from langchain-core<2.0.0,>=1.2.0->langchain-text-splitters>=0.0.1->projectmind==0.4.0)
2026-01-26T14:30:59.0135128Z   Downloading langsmith-0.6.4-py3-none-any.whl.metadata (15 kB)
2026-01-26T14:30:59.0251053Z Collecting packaging>=22.0 (from black>=23.0.0->projectmind==0.4.0)
2026-01-26T14:30:59.0285978Z   Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
2026-01-26T14:30:59.1287939Z Collecting uuid-utils<1.0,>=0.12.0 (from langchain-core<2.0.0,>=1.2.0->langchain-text-splitters>=0.0.1->projectmind==0.4.0)
2026-01-26T14:30:59.1327090Z   Downloading uuid_utils-0.14.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
2026-01-26T14:30:59.1491721Z Collecting jsonpointer>=1.9 (from jsonpatch<2.0.0,>=1.33.0->langchain-core<2.0.0,>=1.2.0->langchain-text-splitters>=0.0.1->projectmind==0.4.0)
2026-01-26T14:30:59.1522824Z   Downloading jsonpointer-3.0.0-py2.py3-none-any.whl.metadata (2.3 kB)
2026-01-26T14:30:59.1999739Z Collecting requests-toolbelt>=1.0.0 (from langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.2.0->langchain-text-splitters>=0.0.1->projectmind==0.4.0)
2026-01-26T14:30:59.2033269Z   Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
2026-01-26T14:30:59.3076844Z Collecting zstandard>=0.23.0 (from langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.2.0->langchain-text-splitters>=0.0.1->projectmind==0.4.0)
2026-01-26T14:30:59.3118470Z   Downloading zstandard-0.25.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (3.3 kB)
2026-01-26T14:30:59.3286728Z Collecting annotated-types>=0.6.0 (from pydantic>=1.9->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:30:59.3318084Z   Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
2026-01-26T14:31:00.2445740Z Collecting pydantic-core==2.41.5 (from pydantic>=1.9->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:00.2484965Z   Downloading pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
2026-01-26T14:31:00.2671857Z Collecting typing-inspection>=0.4.2 (from pydantic>=1.9->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:00.2705652Z   Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
2026-01-26T14:31:00.3060097Z Collecting httpx-sse>=0.4 (from mcp>=0.1.0->projectmind==0.4.0)
2026-01-26T14:31:00.3097005Z   Downloading httpx_sse-0.4.3-py3-none-any.whl.metadata (9.7 kB)
2026-01-26T14:31:00.3393341Z Collecting pydantic-settings>=2.5.2 (from mcp>=0.1.0->projectmind==0.4.0)
2026-01-26T14:31:00.3462295Z   Downloading pydantic_settings-2.12.0-py3-none-any.whl.metadata (3.4 kB)
2026-01-26T14:31:00.3859002Z Collecting pyjwt>=2.10.1 (from pyjwt[crypto]>=2.10.1->mcp>=0.1.0->projectmind==0.4.0)
2026-01-26T14:31:00.3893163Z   Downloading PyJWT-2.10.1-py3-none-any.whl.metadata (4.0 kB)
2026-01-26T14:31:00.4067859Z Collecting python-multipart>=0.0.9 (from mcp>=0.1.0->projectmind==0.4.0)
2026-01-26T14:31:00.4109879Z   Downloading python_multipart-0.0.22-py3-none-any.whl.metadata (1.8 kB)
2026-01-26T14:31:00.4611960Z Collecting sse-starlette>=1.6.1 (from mcp>=0.1.0->projectmind==0.4.0)
2026-01-26T14:31:00.4649494Z   Downloading sse_starlette-3.2.0-py3-none-any.whl.metadata (12 kB)
2026-01-26T14:31:00.5681569Z Collecting starlette>=0.27 (from mcp>=0.1.0->projectmind==0.4.0)
2026-01-26T14:31:00.5718378Z   Downloading starlette-0.52.1-py3-none-any.whl.metadata (6.3 kB)
2026-01-26T14:31:00.6113396Z Collecting exceptiongroup>=1.0.2 (from anyio->httpx>=0.27.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:00.6149445Z   Downloading exceptiongroup-1.3.1-py3-none-any.whl.metadata (6.7 kB)
2026-01-26T14:31:00.7588275Z Collecting librt>=0.6.2 (from mypy>=1.0.0->projectmind==0.4.0)
2026-01-26T14:31:00.7639459Z   Downloading librt-0.7.8-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (1.3 kB)
2026-01-26T14:31:00.7926254Z Collecting coloredlogs (from onnxruntime>=1.14.1->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:00.7962298Z   Downloading coloredlogs-15.0.1-py2.py3-none-any.whl.metadata (12 kB)
2026-01-26T14:31:00.8122387Z Collecting flatbuffers (from onnxruntime>=1.14.1->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:00.8159257Z   Downloading flatbuffers-25.12.19-py2.py3-none-any.whl.metadata (1.0 kB)
2026-01-26T14:31:01.1687465Z Collecting protobuf (from onnxruntime>=1.14.1->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:01.1724186Z   Downloading protobuf-6.33.4-cp39-abi3-manylinux2014_x86_64.whl.metadata (593 bytes)
2026-01-26T14:31:01.1915826Z Collecting sympy (from onnxruntime>=1.14.1->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:01.1953121Z   Downloading sympy-1.14.0-py3-none-any.whl.metadata (12 kB)
2026-01-26T14:31:01.2362304Z Collecting importlib-metadata<8.8.0,>=6.0 (from opentelemetry-api>=1.2.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:01.2409451Z   Downloading importlib_metadata-8.7.1-py3-none-any.whl.metadata (4.7 kB)
2026-01-26T14:31:01.2710302Z Collecting zipp>=3.20 (from importlib-metadata<8.8.0,>=6.0->opentelemetry-api>=1.2.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:01.2867190Z   Downloading zipp-3.23.0-py3-none-any.whl.metadata (3.6 kB)
2026-01-26T14:31:01.3182741Z Collecting googleapis-common-protos~=1.57 (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:01.3301791Z   Downloading googleapis_common_protos-1.72.0-py3-none-any.whl.metadata (9.4 kB)
2026-01-26T14:31:01.3733638Z Collecting opentelemetry-exporter-otlp-proto-common==1.39.1 (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:01.3772425Z   Downloading opentelemetry_exporter_otlp_proto_common-1.39.1-py3-none-any.whl.metadata (1.8 kB)
2026-01-26T14:31:01.4006191Z Collecting opentelemetry-proto==1.39.1 (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:01.4045982Z   Downloading opentelemetry_proto-1.39.1-py3-none-any.whl.metadata (2.3 kB)
2026-01-26T14:31:01.5244882Z Collecting opentelemetry-semantic-conventions==0.60b1 (from opentelemetry-sdk>=1.2.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:01.5283505Z   Downloading opentelemetry_semantic_conventions-0.60b1-py3-none-any.whl.metadata (2.4 kB)
2026-01-26T14:31:01.5616770Z Collecting cfgv>=2.0.0 (from pre-commit>=3.0.0->projectmind==0.4.0)
2026-01-26T14:31:01.5655532Z   Downloading cfgv-3.5.0-py2.py3-none-any.whl.metadata (8.9 kB)
2026-01-26T14:31:01.6218167Z Collecting identify>=1.0.0 (from pre-commit>=3.0.0->projectmind==0.4.0)
2026-01-26T14:31:01.6265913Z   Downloading identify-2.6.16-py2.py3-none-any.whl.metadata (4.4 kB)
2026-01-26T14:31:01.6469529Z Collecting nodeenv>=0.11.1 (from pre-commit>=3.0.0->projectmind==0.4.0)
2026-01-26T14:31:01.6508500Z   Downloading nodeenv-1.10.0-py2.py3-none-any.whl.metadata (24 kB)
2026-01-26T14:31:01.7127801Z Collecting virtualenv>=20.10.0 (from pre-commit>=3.0.0->projectmind==0.4.0)
2026-01-26T14:31:01.7166975Z   Downloading virtualenv-20.36.1-py3-none-any.whl.metadata (4.7 kB)
2026-01-26T14:31:01.7719994Z Collecting python-dotenv>=0.21.0 (from pydantic-settings>=2.5.2->mcp>=0.1.0->projectmind==0.4.0)
2026-01-26T14:31:01.7758233Z   Downloading python_dotenv-1.2.1-py3-none-any.whl.metadata (25 kB)
2026-01-26T14:31:02.0170688Z Collecting cryptography>=3.4.0 (from pyjwt[crypto]>=2.10.1->mcp>=0.1.0->projectmind==0.4.0)
2026-01-26T14:31:02.0210070Z   Downloading cryptography-46.0.3-cp38-abi3-manylinux_2_34_x86_64.whl.metadata (5.7 kB)
2026-01-26T14:31:02.1670171Z Collecting cffi>=2.0.0 (from cryptography>=3.4.0->pyjwt[crypto]>=2.10.1->mcp>=0.1.0->projectmind==0.4.0)
2026-01-26T14:31:02.1707773Z   Downloading cffi-2.0.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
2026-01-26T14:31:02.1956342Z Collecting pycparser (from cffi>=2.0.0->cryptography>=3.4.0->pyjwt[crypto]>=2.10.1->mcp>=0.1.0->projectmind==0.4.0)
2026-01-26T14:31:02.1989528Z   Downloading pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
2026-01-26T14:31:02.2455788Z Collecting astroid<=4.1.dev0,>=4.0.2 (from pylint>=3.0.0->projectmind==0.4.0)
2026-01-26T14:31:02.2497250Z   Downloading astroid-4.0.3-py3-none-any.whl.metadata (4.4 kB)
2026-01-26T14:31:02.2659709Z Collecting dill>=0.2 (from pylint>=3.0.0->projectmind==0.4.0)
2026-01-26T14:31:02.2699330Z   Downloading dill-0.4.1-py3-none-any.whl.metadata (10 kB)
2026-01-26T14:31:02.3167288Z Collecting isort!=5.13,<8,>=5 (from pylint>=3.0.0->projectmind==0.4.0)
2026-01-26T14:31:02.3204688Z   Downloading isort-7.0.0-py3-none-any.whl.metadata (11 kB)
2026-01-26T14:31:02.3345047Z Collecting mccabe<0.8,>=0.6 (from pylint>=3.0.0->projectmind==0.4.0)
2026-01-26T14:31:02.3383784Z   Downloading mccabe-0.7.0-py2.py3-none-any.whl.metadata (5.0 kB)
2026-01-26T14:31:02.3717158Z Collecting tomlkit>=0.10.1 (from pylint>=3.0.0->projectmind==0.4.0)
2026-01-26T14:31:02.3757742Z   Downloading tomlkit-0.14.0-py3-none-any.whl.metadata (2.8 kB)
2026-01-26T14:31:02.4168192Z Collecting iniconfig>=1.0.1 (from pytest>=7.0.0->projectmind==0.4.0)
2026-01-26T14:31:02.4203972Z   Downloading iniconfig-2.3.0-py3-none-any.whl.metadata (2.5 kB)
2026-01-26T14:31:02.4355890Z Collecting pluggy<2,>=1.5 (from pytest>=7.0.0->projectmind==0.4.0)
2026-01-26T14:31:02.4391769Z   Downloading pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
2026-01-26T14:31:02.4635344Z Collecting pygments>=2.7.2 (from pytest>=7.0.0->projectmind==0.4.0)
2026-01-26T14:31:02.4675639Z   Downloading pygments-2.19.2-py3-none-any.whl.metadata (2.5 kB)
2026-01-26T14:31:02.9516676Z Collecting coverage>=7.10.6 (from coverage[toml]>=7.10.6->pytest-cov>=4.0.0->projectmind==0.4.0)
2026-01-26T14:31:02.9614094Z   Downloading coverage-7.13.2-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (8.5 kB)
2026-01-26T14:31:03.0000934Z Collecting mando<0.8,>=0.6 (from radon>=6.0.0->projectmind==0.4.0)
2026-01-26T14:31:03.0051281Z   Downloading mando-0.7.1-py2.py3-none-any.whl.metadata (7.4 kB)
2026-01-26T14:31:03.0243687Z Collecting colorama>=0.4.1 (from radon>=6.0.0->projectmind==0.4.0)
2026-01-26T14:31:03.0282488Z   Downloading colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
2026-01-26T14:31:03.0976817Z Collecting markdown-it-py>=2.2.0 (from rich>=10.11.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:03.1010184Z   Downloading markdown_it_py-4.0.0-py3-none-any.whl.metadata (7.3 kB)
2026-01-26T14:31:03.1266041Z Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=10.11.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:03.1307529Z   Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
2026-01-26T14:31:03.2024796Z Collecting transformers<6.0.0,>=4.41.0 (from sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:03.2064625Z   Downloading transformers-5.0.0-py3-none-any.whl.metadata (37 kB)
2026-01-26T14:31:03.6124907Z Collecting torch>=1.11.0 (from sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:03.6163012Z   Downloading torch-2.10.0-cp310-cp310-manylinux_2_28_x86_64.whl.metadata (31 kB)
2026-01-26T14:31:03.7353829Z Collecting scikit-learn (from sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:03.7397687Z   Downloading scikit_learn-1.7.2-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (11 kB)
2026-01-26T14:31:03.9195295Z Collecting scipy (from sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:03.9236925Z   Downloading scipy-1.15.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (61 kB)
2026-01-26T14:31:03.9879444Z Collecting huggingface-hub>=0.20.0 (from sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:03.9917499Z   Downloading huggingface_hub-1.3.4-py3-none-any.whl.metadata (13 kB)
2026-01-26T14:31:04.0519300Z Collecting filelock (from transformers<6.0.0,>=4.41.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:04.0564255Z   Downloading filelock-3.20.3-py3-none-any.whl.metadata (2.1 kB)
2026-01-26T14:31:04.5560028Z Collecting regex!=2019.12.17 (from transformers<6.0.0,>=4.41.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:04.5602282Z   Downloading regex-2026.1.15-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (40 kB)
2026-01-26T14:31:04.5877424Z Collecting typer-slim (from transformers<6.0.0,>=4.41.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:04.5913903Z   Downloading typer_slim-0.21.1-py3-none-any.whl.metadata (16 kB)
2026-01-26T14:31:04.7402061Z Collecting safetensors>=0.4.3 (from transformers<6.0.0,>=4.41.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:04.7444950Z   Downloading safetensors-0.7.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB)
2026-01-26T14:31:04.8007914Z Collecting fsspec>=2023.5.0 (from huggingface-hub>=0.20.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:04.8045929Z   Downloading fsspec-2026.1.0-py3-none-any.whl.metadata (10 kB)
2026-01-26T14:31:04.9041519Z Collecting hf-xet<2.0.0,>=1.2.0 (from huggingface-hub>=0.20.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:04.9079689Z   Downloading hf_xet-1.2.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
2026-01-26T14:31:04.9301275Z Collecting shellingham (from huggingface-hub>=0.20.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:04.9340859Z   Downloading shellingham-1.5.4-py2.py3-none-any.whl.metadata (3.5 kB)
2026-01-26T14:31:05.0949202Z Collecting networkx>=2.5.1 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.0986443Z   Downloading networkx-3.4.2-py3-none-any.whl.metadata (6.3 kB)
2026-01-26T14:31:05.1236818Z Collecting jinja2 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.1272749Z   Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
2026-01-26T14:31:05.1640509Z Collecting cuda-bindings==12.9.4 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.1679933Z   Downloading cuda_bindings-12.9.4-cp310-cp310-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (2.6 kB)
2026-01-26T14:31:05.1851585Z Collecting nvidia-cuda-nvrtc-cu12==12.8.93 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.1886345Z   Downloading nvidia_cuda_nvrtc_cu12-12.8.93-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl.metadata (1.7 kB)
2026-01-26T14:31:05.2046902Z Collecting nvidia-cuda-runtime-cu12==12.8.90 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.2083445Z   Downloading nvidia_cuda_runtime_cu12-12.8.90-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.7 kB)
2026-01-26T14:31:05.2233793Z Collecting nvidia-cuda-cupti-cu12==12.8.90 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.2270257Z   Downloading nvidia_cuda_cupti_cu12-12.8.90-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.7 kB)
2026-01-26T14:31:05.2469333Z Collecting nvidia-cudnn-cu12==9.10.2.21 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.2507169Z   Downloading nvidia_cudnn_cu12-9.10.2.21-py3-none-manylinux_2_27_x86_64.whl.metadata (1.8 kB)
2026-01-26T14:31:05.2665618Z Collecting nvidia-cublas-cu12==12.8.4.1 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.2731065Z   Downloading nvidia_cublas_cu12-12.8.4.1-py3-none-manylinux_2_27_x86_64.whl.metadata (1.7 kB)
2026-01-26T14:31:05.2890891Z Collecting nvidia-cufft-cu12==11.3.3.83 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.2930264Z   Downloading nvidia_cufft_cu12-11.3.3.83-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.7 kB)
2026-01-26T14:31:05.3155960Z Collecting nvidia-curand-cu12==10.3.9.90 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.3193726Z   Downloading nvidia_curand_cu12-10.3.9.90-py3-none-manylinux_2_27_x86_64.whl.metadata (1.7 kB)
2026-01-26T14:31:05.3353719Z Collecting nvidia-cusolver-cu12==11.7.3.90 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.3391682Z   Downloading nvidia_cusolver_cu12-11.7.3.90-py3-none-manylinux_2_27_x86_64.whl.metadata (1.8 kB)
2026-01-26T14:31:05.3547318Z Collecting nvidia-cusparse-cu12==12.5.8.93 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.3590035Z   Downloading nvidia_cusparse_cu12-12.5.8.93-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.8 kB)
2026-01-26T14:31:05.3725681Z Collecting nvidia-cusparselt-cu12==0.7.1 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.3769641Z   Downloading nvidia_cusparselt_cu12-0.7.1-py3-none-manylinux2014_x86_64.whl.metadata (7.0 kB)
2026-01-26T14:31:05.3942646Z Collecting nvidia-nccl-cu12==2.27.5 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.4006372Z   Downloading nvidia_nccl_cu12-2.27.5-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.0 kB)
2026-01-26T14:31:05.4138414Z Collecting nvidia-nvshmem-cu12==3.4.5 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.4175234Z   Downloading nvidia_nvshmem_cu12-3.4.5-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.1 kB)
2026-01-26T14:31:05.4329452Z Collecting nvidia-nvtx-cu12==12.8.90 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.4372486Z   Downloading nvidia_nvtx_cu12-12.8.90-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.8 kB)
2026-01-26T14:31:05.4531815Z Collecting nvidia-nvjitlink-cu12==12.8.93 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.4571757Z   Downloading nvidia_nvjitlink_cu12-12.8.93-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl.metadata (1.7 kB)
2026-01-26T14:31:05.4697261Z Collecting nvidia-cufile-cu12==1.13.1.3 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.4737623Z   Downloading nvidia_cufile_cu12-1.13.1.3-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.7 kB)
2026-01-26T14:31:05.4959662Z Collecting triton==3.6.0 (from torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.5003329Z   Downloading triton-3.6.0-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (1.7 kB)
2026-01-26T14:31:05.5206460Z Collecting cuda-pathfinder~=1.1 (from cuda-bindings==12.9.4->torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:05.5244840Z   Downloading cuda_pathfinder-1.3.3-py3-none-any.whl.metadata (1.9 kB)
2026-01-26T14:31:07.0296783Z Collecting mpmath<1.4,>=1.1.0 (from sympy->onnxruntime>=1.14.1->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:07.0321687Z   Downloading mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
2026-01-26T14:31:07.1328601Z Collecting httptools>=0.6.3 (from uvicorn[standard]>=0.18.3->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:07.1367570Z   Downloading httptools-0.7.1-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (3.5 kB)
2026-01-26T14:31:07.1905086Z Collecting uvloop>=0.15.1 (from uvicorn[standard]>=0.18.3->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:07.1942025Z   Downloading uvloop-0.22.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.9 kB)
2026-01-26T14:31:07.2941449Z Collecting watchfiles>=0.13 (from uvicorn[standard]>=0.18.3->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:07.3035329Z   Downloading watchfiles-1.1.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
2026-01-26T14:31:07.4330276Z Collecting websockets>=10.4 (from uvicorn[standard]>=0.18.3->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:07.4369889Z   Downloading websockets-16.0-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (6.8 kB)
2026-01-26T14:31:07.4671203Z Collecting distlib<1,>=0.3.7 (from virtualenv>=20.10.0->pre-commit>=3.0.0->projectmind==0.4.0)
2026-01-26T14:31:07.4709872Z   Downloading distlib-0.4.0-py2.py3-none-any.whl.metadata (5.2 kB)
2026-01-26T14:31:07.5593730Z Collecting humanfriendly>=9.1 (from coloredlogs->onnxruntime>=1.14.1->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:07.5632840Z   Downloading humanfriendly-10.0-py2.py3-none-any.whl.metadata (9.2 kB)
2026-01-26T14:31:07.8547552Z Collecting MarkupSafe>=2.0 (from jinja2->torch>=1.11.0->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:07.8591194Z   Downloading markupsafe-3.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
2026-01-26T14:31:07.8986974Z Collecting oauthlib>=3.0.0 (from requests-oauthlib->kubernetes>=28.1.0->chromadb>=0.4.0->projectmind==0.4.0)
2026-01-26T14:31:07.9027930Z   Downloading oauthlib-3.3.1-py3-none-any.whl.metadata (7.9 kB)
2026-01-26T14:31:07.9592649Z Collecting joblib>=1.2.0 (from scikit-learn->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:07.9633493Z   Downloading joblib-1.5.3-py3-none-any.whl.metadata (5.5 kB)
2026-01-26T14:31:07.9765439Z Collecting threadpoolctl>=3.1.0 (from scikit-learn->sentence-transformers>=2.2.0->projectmind==0.4.0)
2026-01-26T14:31:07.9806072Z   Downloading threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)
2026-01-26T14:31:08.0307013Z Downloading black-26.1.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (1.8 MB)
2026-01-26T14:31:08.0470604Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 131.5 MB/s  0:00:00
2026-01-26T14:31:08.0549217Z Downloading chromadb-1.4.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (21.1 MB)
2026-01-26T14:31:08.1592932Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 21.1/21.1 MB 206.5 MB/s  0:00:00
2026-01-26T14:31:08.1632282Z Downloading posthog-5.4.0-py3-none-any.whl (105 kB)
2026-01-26T14:31:08.1699204Z Downloading requests-2.32.5-py3-none-any.whl (64 kB)
2026-01-26T14:31:08.1759374Z Downloading charset_normalizer-3.4.4-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (153 kB)
2026-01-26T14:31:08.1825203Z Downloading idna-3.11-py3-none-any.whl (71 kB)
2026-01-26T14:31:08.1879707Z Downloading urllib3-2.6.3-py3-none-any.whl (131 kB)
2026-01-26T14:31:08.1934569Z Downloading backoff-2.2.1-py3-none-any.whl (15 kB)
2026-01-26T14:31:08.1989442Z Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl (278 kB)
2026-01-26T14:31:08.2055596Z Downloading build-1.4.0-py3-none-any.whl (24 kB)
2026-01-26T14:31:08.2110141Z Downloading certifi-2026.1.4-py3-none-any.whl (152 kB)
2026-01-26T14:31:08.2180182Z Downloading click-8.3.1-py3-none-any.whl (108 kB)
2026-01-26T14:31:08.2236696Z Downloading distro-1.9.0-py3-none-any.whl (20 kB)
2026-01-26T14:31:08.2289766Z Downloading gitpython-3.1.46-py3-none-any.whl (208 kB)
2026-01-26T14:31:08.2348328Z Downloading gitdb-4.0.12-py3-none-any.whl (62 kB)
2026-01-26T14:31:08.2402154Z Downloading smmap-5.0.2-py3-none-any.whl (24 kB)
2026-01-26T14:31:08.2466463Z Downloading grpcio-1.76.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (6.6 MB)
2026-01-26T14:31:08.2798465Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.6/6.6 MB 218.5 MB/s  0:00:00
2026-01-26T14:31:08.2835359Z Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
2026-01-26T14:31:08.2891247Z Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
2026-01-26T14:31:08.3001336Z Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
2026-01-26T14:31:08.3058679Z Downloading h11-0.16.0-py3-none-any.whl (37 kB)
2026-01-26T14:31:08.3111936Z Downloading jsonschema-4.26.0-py3-none-any.whl (90 kB)
2026-01-26T14:31:08.3167721Z Downloading attrs-25.4.0-py3-none-any.whl (67 kB)
2026-01-26T14:31:08.3221205Z Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
2026-01-26T14:31:08.3287023Z Downloading kubernetes-35.0.0-py2.py3-none-any.whl (2.0 MB)
2026-01-26T14:31:08.3412650Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 196.7 MB/s  0:00:00
2026-01-26T14:31:08.3450197Z Downloading durationpy-0.10-py3-none-any.whl (3.9 kB)
2026-01-26T14:31:08.3504488Z Downloading langchain_text_splitters-1.1.0-py3-none-any.whl (34 kB)
2026-01-26T14:31:08.3567251Z Downloading langchain_core-1.2.7-py3-none-any.whl (490 kB)
2026-01-26T14:31:08.3643614Z Downloading jsonpatch-1.33-py2.py3-none-any.whl (12 kB)
2026-01-26T14:31:08.3701199Z Downloading langsmith-0.6.4-py3-none-any.whl (283 kB)
2026-01-26T14:31:08.3767816Z Downloading packaging-25.0-py3-none-any.whl (66 kB)
2026-01-26T14:31:08.3835977Z Downloading pydantic-2.12.5-py3-none-any.whl (463 kB)
2026-01-26T14:31:08.3914327Z Downloading pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
2026-01-26T14:31:08.4036007Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 199.1 MB/s  0:00:00
2026-01-26T14:31:08.4076269Z Downloading pyyaml-6.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (770 kB)
2026-01-26T14:31:08.4153303Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 770.3/770.3 kB 116.7 MB/s  0:00:00
2026-01-26T14:31:08.4191831Z Downloading tenacity-9.1.2-py3-none-any.whl (28 kB)
2026-01-26T14:31:08.4253350Z Downloading uuid_utils-0.14.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (341 kB)
2026-01-26T14:31:08.4319193Z Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
2026-01-26T14:31:08.4371198Z Downloading jsonpointer-3.0.0-py2.py3-none-any.whl (7.6 kB)
2026-01-26T14:31:08.4441605Z Downloading mcp-1.26.0-py3-none-any.whl (233 kB)
2026-01-26T14:31:08.4502610Z Downloading anyio-4.12.1-py3-none-any.whl (113 kB)
2026-01-26T14:31:08.4561092Z Downloading exceptiongroup-1.3.1-py3-none-any.whl (16 kB)
2026-01-26T14:31:08.4615158Z Downloading httpx_sse-0.4.3-py3-none-any.whl (9.0 kB)
2026-01-26T14:31:08.4674094Z Downloading mmh3-5.2.0-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (101 kB)
2026-01-26T14:31:08.4739193Z Downloading mypy-1.19.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (13.5 MB)
2026-01-26T14:31:08.5422519Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.5/13.5 MB 205.2 MB/s  0:00:00
2026-01-26T14:31:08.5464204Z Downloading librt-0.7.8-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (186 kB)
2026-01-26T14:31:08.5529539Z Downloading mypy_extensions-1.1.0-py3-none-any.whl (5.0 kB)
2026-01-26T14:31:08.5591820Z Downloading numpy-2.2.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
2026-01-26T14:31:08.6306034Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.8/16.8 MB 243.4 MB/s  0:00:00
2026-01-26T14:31:08.6376830Z Downloading onnxruntime-1.23.2-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (17.4 MB)
2026-01-26T14:31:08.7124453Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 17.4/17.4 MB 239.6 MB/s  0:00:00
2026-01-26T14:31:08.7163843Z Downloading opentelemetry_api-1.39.1-py3-none-any.whl (66 kB)
2026-01-26T14:31:08.7225432Z Downloading importlib_metadata-8.7.1-py3-none-any.whl (27 kB)
2026-01-26T14:31:08.7278726Z Downloading opentelemetry_exporter_otlp_proto_grpc-1.39.1-py3-none-any.whl (19 kB)
2026-01-26T14:31:08.7331096Z Downloading opentelemetry_exporter_otlp_proto_common-1.39.1-py3-none-any.whl (18 kB)
2026-01-26T14:31:08.7388153Z Downloading opentelemetry_proto-1.39.1-py3-none-any.whl (72 kB)
2026-01-26T14:31:08.7443987Z Downloading googleapis_common_protos-1.72.0-py3-none-any.whl (297 kB)
2026-01-26T14:31:08.7518087Z Downloading opentelemetry_sdk-1.39.1-py3-none-any.whl (132 kB)
2026-01-26T14:31:08.7582372Z Downloading opentelemetry_semantic_conventions-0.60b1-py3-none-any.whl (219 kB)
2026-01-26T14:31:08.7644100Z Downloading protobuf-6.33.4-cp39-abi3-manylinux2014_x86_64.whl (323 kB)
2026-01-26T14:31:08.7713324Z Downloading orjson-3.11.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (139 kB)
2026-01-26T14:31:08.7772411Z Downloading overrides-7.7.0-py3-none-any.whl (17 kB)
2026-01-26T14:31:08.7824623Z Downloading pathspec-1.0.3-py3-none-any.whl (55 kB)
2026-01-26T14:31:08.7878565Z Downloading platformdirs-4.5.1-py3-none-any.whl (18 kB)
2026-01-26T14:31:08.7934653Z Downloading pre_commit-4.5.1-py2.py3-none-any.whl (226 kB)
2026-01-26T14:31:08.7999154Z Downloading cfgv-3.5.0-py2.py3-none-any.whl (7.4 kB)
2026-01-26T14:31:08.8057946Z Downloading identify-2.6.16-py2.py3-none-any.whl (99 kB)
2026-01-26T14:31:08.8119967Z Downloading nodeenv-1.10.0-py2.py3-none-any.whl (23 kB)
2026-01-26T14:31:08.8194877Z Downloading pybase64-1.4.3-cp310-cp310-manylinux1_x86_64.manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_5_x86_64.whl (68 kB)
2026-01-26T14:31:08.8252715Z Downloading pydantic_settings-2.12.0-py3-none-any.whl (51 kB)
2026-01-26T14:31:08.8311364Z Downloading PyJWT-2.10.1-py3-none-any.whl (22 kB)
2026-01-26T14:31:08.8386223Z Downloading cryptography-46.0.3-cp38-abi3-manylinux_2_34_x86_64.whl (4.5 MB)
2026-01-26T14:31:08.8600185Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 215.0 MB/s  0:00:00
2026-01-26T14:31:08.8641255Z Downloading cffi-2.0.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (216 kB)
2026-01-26T14:31:08.8713935Z Downloading pylint-4.0.4-py3-none-any.whl (536 kB)
2026-01-26T14:31:08.8905112Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.4/536.4 kB 19.4 MB/s  0:00:00
2026-01-26T14:31:08.8956603Z Downloading astroid-4.0.3-py3-none-any.whl (276 kB)
2026-01-26T14:31:08.9032462Z Downloading isort-7.0.0-py3-none-any.whl (94 kB)
2026-01-26T14:31:08.9093150Z Downloading mccabe-0.7.0-py2.py3-none-any.whl (7.3 kB)
2026-01-26T14:31:08.9171344Z Downloading dill-0.4.1-py3-none-any.whl (120 kB)
2026-01-26T14:31:08.9249954Z Downloading pypika-0.50.0-py2.py3-none-any.whl (60 kB)
2026-01-26T14:31:08.9323286Z Downloading pytest-9.0.2-py3-none-any.whl (374 kB)
2026-01-26T14:31:08.9400414Z Downloading pluggy-1.6.0-py3-none-any.whl (20 kB)
2026-01-26T14:31:08.9470745Z Downloading iniconfig-2.3.0-py3-none-any.whl (7.5 kB)
2026-01-26T14:31:08.9538708Z Downloading pygments-2.19.2-py3-none-any.whl (1.2 MB)
2026-01-26T14:31:08.9631780Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 157.2 MB/s  0:00:00
2026-01-26T14:31:08.9675800Z Downloading pytest_cov-7.0.0-py3-none-any.whl (22 kB)
2026-01-26T14:31:08.9742025Z Downloading coverage-7.13.2-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (247 kB)
2026-01-26T14:31:08.9816387Z Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
2026-01-26T14:31:08.9894777Z Downloading python_dotenv-1.2.1-py3-none-any.whl (21 kB)
2026-01-26T14:31:08.9953955Z Downloading python_multipart-0.0.22-py3-none-any.whl (24 kB)
2026-01-26T14:31:09.0013826Z Downloading pytokens-0.4.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (258 kB)
2026-01-26T14:31:09.0083224Z Downloading radon-6.0.1-py2.py3-none-any.whl (52 kB)
2026-01-26T14:31:09.0138425Z Downloading mando-0.7.1-py2.py3-none-any.whl (28 kB)
2026-01-26T14:31:09.0200519Z Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
2026-01-26T14:31:09.0255568Z Downloading referencing-0.37.0-py3-none-any.whl (26 kB)
2026-01-26T14:31:09.0327326Z Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
2026-01-26T14:31:09.0389590Z Downloading rich-14.3.1-py3-none-any.whl (309 kB)
2026-01-26T14:31:09.0475337Z Downloading markdown_it_py-4.0.0-py3-none-any.whl (87 kB)
2026-01-26T14:31:09.0539722Z Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
2026-01-26T14:31:09.0600266Z Downloading rpds_py-0.30.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (390 kB)
2026-01-26T14:31:09.0692852Z Downloading ruff-0.14.14-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.2 MB)
2026-01-26T14:31:09.1200650Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.2/11.2 MB 228.0 MB/s  0:00:00
2026-01-26T14:31:09.1244110Z Downloading sentence_transformers-5.2.0-py3-none-any.whl (493 kB)
2026-01-26T14:31:09.1369345Z Downloading transformers-5.0.0-py3-none-any.whl (10.1 MB)
2026-01-26T14:31:09.1946232Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.1/10.1 MB 180.6 MB/s  0:00:00
2026-01-26T14:31:09.1987463Z Downloading huggingface_hub-1.3.4-py3-none-any.whl (536 kB)
2026-01-26T14:31:09.2054459Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.6/536.6 kB 78.9 MB/s  0:00:00
2026-01-26T14:31:09.2100271Z Downloading hf_xet-1.2.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.3 MB)
2026-01-26T14:31:09.2283484Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 221.7 MB/s  0:00:00
2026-01-26T14:31:09.2324923Z Downloading tokenizers-0.22.2-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.3 MB)
2026-01-26T14:31:09.2499832Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 209.6 MB/s  0:00:00
2026-01-26T14:31:09.2538280Z Downloading fsspec-2026.1.0-py3-none-any.whl (201 kB)
2026-01-26T14:31:09.2612302Z Downloading regex-2026.1.15-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (791 kB)
2026-01-26T14:31:09.2685726Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 791.8/791.8 kB 122.9 MB/s  0:00:00
2026-01-26T14:31:09.2731937Z Downloading safetensors-0.7.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (507 kB)
2026-01-26T14:31:09.2813007Z Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
2026-01-26T14:31:09.2866827Z Downloading sse_starlette-3.2.0-py3-none-any.whl (12 kB)
2026-01-26T14:31:09.3030091Z Downloading starlette-0.52.1-py3-none-any.whl (74 kB)
2026-01-26T14:31:09.3091288Z Downloading tomli-2.4.0-py3-none-any.whl (14 kB)
2026-01-26T14:31:09.3147725Z Downloading tomlkit-0.14.0-py3-none-any.whl (39 kB)
2026-01-26T14:31:09.3248354Z Downloading torch-2.10.0-cp310-cp310-manylinux_2_28_x86_64.whl (915.6 MB)
2026-01-26T14:31:23.7987492Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 915.6/915.6 MB 21.5 MB/s  0:00:14
2026-01-26T14:31:23.8031831Z Downloading cuda_bindings-12.9.4-cp310-cp310-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (12.1 MB)
2026-01-26T14:31:23.8557444Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.1/12.1 MB 240.3 MB/s  0:00:00
2026-01-26T14:31:23.8597655Z Downloading nvidia_cublas_cu12-12.8.4.1-py3-none-manylinux_2_27_x86_64.whl (594.3 MB)
2026-01-26T14:31:31.8467672Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 594.3/594.3 MB 36.9 MB/s  0:00:07
2026-01-26T14:31:31.8519054Z Downloading nvidia_cuda_cupti_cu12-12.8.90-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (10.2 MB)
2026-01-26T14:31:31.9023913Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.2/10.2 MB 211.1 MB/s  0:00:00
2026-01-26T14:31:31.9067314Z Downloading nvidia_cuda_nvrtc_cu12-12.8.93-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl (88.0 MB)
2026-01-26T14:31:32.3418520Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 88.0/88.0 MB 203.4 MB/s  0:00:00
2026-01-26T14:31:32.3475117Z Downloading nvidia_cuda_runtime_cu12-12.8.90-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (954 kB)
2026-01-26T14:31:32.3564201Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 954.8/954.8 kB 133.0 MB/s  0:00:00
2026-01-26T14:31:32.3618714Z Downloading nvidia_cudnn_cu12-9.10.2.21-py3-none-manylinux_2_27_x86_64.whl (706.8 MB)
2026-01-26T14:31:43.4261681Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 706.8/706.8 MB 27.1 MB/s  0:00:11
2026-01-26T14:31:43.4346981Z Downloading nvidia_cufft_cu12-11.3.3.83-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (193.1 MB)
2026-01-26T14:31:45.2751602Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 193.1/193.1 MB 105.0 MB/s  0:00:01
2026-01-26T14:31:45.2796098Z Downloading nvidia_cufile_cu12-1.13.1.3-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (1.2 MB)
2026-01-26T14:31:45.2884833Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 156.8 MB/s  0:00:00
2026-01-26T14:31:45.2930605Z Downloading nvidia_curand_cu12-10.3.9.90-py3-none-manylinux_2_27_x86_64.whl (63.6 MB)
2026-01-26T14:31:45.5907588Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.6/63.6 MB 216.1 MB/s  0:00:00
2026-01-26T14:31:45.5956284Z Downloading nvidia_cusolver_cu12-11.7.3.90-py3-none-manylinux_2_27_x86_64.whl (267.5 MB)
2026-01-26T14:31:49.3322150Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 267.5/267.5 MB 70.5 MB/s  0:00:03
2026-01-26T14:31:49.3372995Z Downloading nvidia_cusparse_cu12-12.5.8.93-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (288.2 MB)
2026-01-26T14:31:52.5330477Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 288.2/288.2 MB 83.9 MB/s  0:00:03
2026-01-26T14:31:52.5377258Z Downloading nvidia_cusparselt_cu12-0.7.1-py3-none-manylinux2014_x86_64.whl (287.2 MB)
2026-01-26T14:31:56.4398167Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 287.2/287.2 MB 68.6 MB/s  0:00:03
2026-01-26T14:31:56.4452356Z Downloading nvidia_nccl_cu12-2.27.5-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (322.3 MB)
2026-01-26T14:32:00.4540867Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 322.3/322.3 MB 68.6 MB/s  0:00:04
2026-01-26T14:32:00.4595441Z Downloading nvidia_nvjitlink_cu12-12.8.93-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl (39.3 MB)
2026-01-26T14:32:00.8325405Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 39.3/39.3 MB 105.7 MB/s  0:00:00
2026-01-26T14:32:00.8367247Z Downloading nvidia_nvshmem_cu12-3.4.5-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (139.1 MB)
2026-01-26T14:32:01.7642012Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 139.1/139.1 MB 150.2 MB/s  0:00:00
2026-01-26T14:32:01.7684669Z Downloading nvidia_nvtx_cu12-12.8.90-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (89 kB)
2026-01-26T14:32:01.7752021Z Downloading triton-3.6.0-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (188.1 MB)
2026-01-26T14:32:03.9667690Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 188.1/188.1 MB 85.8 MB/s  0:00:02
2026-01-26T14:32:03.9707209Z Downloading cuda_pathfinder-1.3.3-py3-none-any.whl (27 kB)
2026-01-26T14:32:03.9776734Z Downloading networkx-3.4.2-py3-none-any.whl (1.7 MB)
2026-01-26T14:32:03.9883082Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 175.9 MB/s  0:00:00
2026-01-26T14:32:03.9954686Z Downloading sympy-1.14.0-py3-none-any.whl (6.3 MB)
2026-01-26T14:32:04.0241130Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.3/6.3 MB 230.6 MB/s  0:00:00
2026-01-26T14:32:04.0381167Z Downloading mpmath-1.3.0-py3-none-any.whl (536 kB)
2026-01-26T14:32:04.0447788Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.2/536.2 kB 74.7 MB/s  0:00:00
2026-01-26T14:32:04.0485335Z Downloading tqdm-4.67.1-py3-none-any.whl (78 kB)
2026-01-26T14:32:04.0545586Z Downloading typer-0.21.1-py3-none-any.whl (47 kB)
2026-01-26T14:32:04.0602591Z Downloading shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)
2026-01-26T14:32:04.0657723Z Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
2026-01-26T14:32:04.0717699Z Downloading uvicorn-0.40.0-py3-none-any.whl (68 kB)
2026-01-26T14:32:04.0800054Z Downloading httptools-0.7.1-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (440 kB)
2026-01-26T14:32:04.0881271Z Downloading uvloop-0.22.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.7 MB)
2026-01-26T14:32:04.1080587Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.7/3.7 MB 208.0 MB/s  0:00:00
2026-01-26T14:32:04.1123415Z Downloading virtualenv-20.36.1-py3-none-any.whl (6.0 MB)
2026-01-26T14:32:04.1429946Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.0/6.0 MB 211.1 MB/s  0:00:00
2026-01-26T14:32:04.1473492Z Downloading distlib-0.4.0-py2.py3-none-any.whl (469 kB)
2026-01-26T14:32:04.1554002Z Downloading filelock-3.20.3-py3-none-any.whl (16 kB)
2026-01-26T14:32:04.1613873Z Downloading watchfiles-1.1.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (455 kB)
2026-01-26T14:32:04.1741461Z Downloading websocket_client-1.9.0-py3-none-any.whl (82 kB)
2026-01-26T14:32:04.1801948Z Downloading websockets-16.0-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (183 kB)
2026-01-26T14:32:04.1864320Z Downloading zipp-3.23.0-py3-none-any.whl (10 kB)
2026-01-26T14:32:04.1923012Z Downloading zstandard-0.25.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (5.6 MB)
2026-01-26T14:32:04.2193048Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.6/5.6 MB 218.6 MB/s  0:00:00
2026-01-26T14:32:04.2233534Z Downloading coloredlogs-15.0.1-py2.py3-none-any.whl (46 kB)
2026-01-26T14:32:04.2293341Z Downloading humanfriendly-10.0-py2.py3-none-any.whl (86 kB)
2026-01-26T14:32:04.2352868Z Downloading flatbuffers-25.12.19-py2.py3-none-any.whl (26 kB)
2026-01-26T14:32:04.2410891Z Downloading importlib_resources-6.5.2-py3-none-any.whl (37 kB)
2026-01-26T14:32:04.2488590Z Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
2026-01-26T14:32:04.2549053Z Downloading markupsafe-3.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (20 kB)
2026-01-26T14:32:04.2611385Z Downloading pycparser-3.0-py3-none-any.whl (48 kB)
2026-01-26T14:32:04.2688358Z Downloading pyproject_hooks-1.2.0-py3-none-any.whl (10 kB)
2026-01-26T14:32:04.2744240Z Downloading requests_oauthlib-2.0.0-py2.py3-none-any.whl (24 kB)
2026-01-26T14:32:04.2800342Z Downloading oauthlib-3.3.1-py3-none-any.whl (160 kB)
2026-01-26T14:32:04.2884312Z Downloading scikit_learn-1.7.2-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (9.7 MB)
2026-01-26T14:32:04.3373052Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.7/9.7 MB 210.4 MB/s  0:00:00
2026-01-26T14:32:04.3410524Z Downloading joblib-1.5.3-py3-none-any.whl (309 kB)
2026-01-26T14:32:04.3489451Z Downloading scipy-1.15.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (37.7 MB)
2026-01-26T14:32:04.5226434Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 37.7/37.7 MB 220.1 MB/s  0:00:00
2026-01-26T14:32:04.5264048Z Downloading threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
2026-01-26T14:32:04.5321360Z Downloading typer_slim-0.21.1-py3-none-any.whl (47 kB)
2026-01-26T14:32:18.8998464Z Building wheels for collected packages: projectmind
2026-01-26T14:32:18.9010957Z   Building editable for projectmind (pyproject.toml): started
2026-01-26T14:32:19.1612732Z   Building editable for projectmind (pyproject.toml): finished with status 'done'
2026-01-26T14:32:19.1620550Z   Created wheel for projectmind: filename=projectmind-0.4.0-0.editable-py3-none-any.whl size=8367 sha256=e326e5d7c707982729f18db5ec79963dfcf51c62c0b12c7cf7a0393abdb026d0
2026-01-26T14:32:19.1622687Z   Stored in directory: /tmp/pip-ephem-wheel-cache-y23f4aww/wheels/86/ef/74/d37cf9775f1d0f87b14c46e6cc2a6ffbc31c7e449acd738d4e
2026-01-26T14:32:19.1643311Z Successfully built projectmind
2026-01-26T14:32:19.8894318Z Installing collected packages: nvidia-cusparselt-cu12, mpmath, flatbuffers, durationpy, distlib, zstandard, zipp, websockets, websocket-client, uvloop, uuid-utils, urllib3, typing-extensions, triton, tqdm, tomlkit, tomli, threadpoolctl, tenacity, sympy, smmap, six, shellingham, safetensors, ruff, rpds-py, regex, pyyaml, pytokens, python-multipart, python-dotenv, pyproject_hooks, pyjwt, pygments, pycparser, pybase64, protobuf, pluggy, platformdirs, pathspec, packaging, overrides, orjson, oauthlib, nvidia-nvtx-cu12, nvidia-nvshmem-cu12, nvidia-nvjitlink-cu12, nvidia-nccl-cu12, nvidia-curand-cu12, nvidia-cufile-cu12, nvidia-cuda-runtime-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-cupti-cu12, nvidia-cublas-cu12, numpy, nodeenv, networkx, mypy-extensions, mmh3, mdurl, mccabe, MarkupSafe, librt, jsonpointer, joblib, isort, iniconfig, importlib-resources, idna, identify, humanfriendly, httpx-sse, httptools, hf-xet, h11, fsspec, filelock, distro, dill, cuda-pathfinder, coverage, colorama, click, charset_normalizer, cfgv, certifi, bcrypt, backoff, attrs, annotated-types, virtualenv, uvicorn, typing-inspection, typer-slim, scipy, requests, referencing, python-dateutil, pypika, pydantic-core, opentelemetry-proto, nvidia-cusparse-cu12, nvidia-cufft-cu12, nvidia-cudnn-cu12, mypy, markdown-it-py, mando, jsonpatch, jinja2, importlib-metadata, httpcore, grpcio, googleapis-common-protos, gitdb, exceptiongroup, cuda-bindings, coloredlogs, cffi, build, black, astroid, scikit-learn, rich, requests-toolbelt, requests-oauthlib, radon, pytest, pylint, pydantic, pre-commit, posthog, opentelemetry-exporter-otlp-proto-common, opentelemetry-api, onnxruntime, nvidia-cusolver-cu12, jsonschema-specifications, GitPython, cryptography, anyio, watchfiles, typer, torch, starlette, pytest-cov, pydantic-settings, opentelemetry-semantic-conventions, kubernetes, jsonschema, httpx, sse-starlette, opentelemetry-sdk, langsmith, huggingface-hub, tokenizers, opentelemetry-exporter-otlp-proto-grpc, mcp, langchain-core, transformers, langchain-text-splitters, chromadb, sentence-transformers, projectmind
2026-01-26T14:33:45.3494051Z 
2026-01-26T14:33:45.3757075Z Successfully installed GitPython-3.1.46 MarkupSafe-3.0.3 annotated-types-0.7.0 anyio-4.12.1 astroid-4.0.3 attrs-25.4.0 backoff-2.2.1 bcrypt-5.0.0 black-26.1.0 build-1.4.0 certifi-2026.1.4 cffi-2.0.0 cfgv-3.5.0 charset_normalizer-3.4.4 chromadb-1.4.1 click-8.3.1 colorama-0.4.6 coloredlogs-15.0.1 coverage-7.13.2 cryptography-46.0.3 cuda-bindings-12.9.4 cuda-pathfinder-1.3.3 dill-0.4.1 distlib-0.4.0 distro-1.9.0 durationpy-0.10 exceptiongroup-1.3.1 filelock-3.20.3 flatbuffers-25.12.19 fsspec-2026.1.0 gitdb-4.0.12 googleapis-common-protos-1.72.0 grpcio-1.76.0 h11-0.16.0 hf-xet-1.2.0 httpcore-1.0.9 httptools-0.7.1 httpx-0.28.1 httpx-sse-0.4.3 huggingface-hub-1.3.4 humanfriendly-10.0 identify-2.6.16 idna-3.11 importlib-metadata-8.7.1 importlib-resources-6.5.2 iniconfig-2.3.0 isort-7.0.0 jinja2-3.1.6 joblib-1.5.3 jsonpatch-1.33 jsonpointer-3.0.0 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 kubernetes-35.0.0 langchain-core-1.2.7 langchain-text-splitters-1.1.0 langsmith-0.6.4 librt-0.7.8 mando-0.7.1 markdown-it-py-4.0.0 mccabe-0.7.0 mcp-1.26.0 mdurl-0.1.2 mmh3-5.2.0 mpmath-1.3.0 mypy-1.19.1 mypy-extensions-1.1.0 networkx-3.4.2 nodeenv-1.10.0 numpy-2.2.6 nvidia-cublas-cu12-12.8.4.1 nvidia-cuda-cupti-cu12-12.8.90 nvidia-cuda-nvrtc-cu12-12.8.93 nvidia-cuda-runtime-cu12-12.8.90 nvidia-cudnn-cu12-9.10.2.21 nvidia-cufft-cu12-11.3.3.83 nvidia-cufile-cu12-1.13.1.3 nvidia-curand-cu12-10.3.9.90 nvidia-cusolver-cu12-11.7.3.90 nvidia-cusparse-cu12-12.5.8.93 nvidia-cusparselt-cu12-0.7.1 nvidia-nccl-cu12-2.27.5 nvidia-nvjitlink-cu12-12.8.93 nvidia-nvshmem-cu12-3.4.5 nvidia-nvtx-cu12-12.8.90 oauthlib-3.3.1 onnxruntime-1.23.2 opentelemetry-api-1.39.1 opentelemetry-exporter-otlp-proto-common-1.39.1 opentelemetry-exporter-otlp-proto-grpc-1.39.1 opentelemetry-proto-1.39.1 opentelemetry-sdk-1.39.1 opentelemetry-semantic-conventions-0.60b1 orjson-3.11.5 overrides-7.7.0 packaging-25.0 pathspec-1.0.3 platformdirs-4.5.1 pluggy-1.6.0 posthog-5.4.0 pre-commit-4.5.1 projectmind-0.4.0 protobuf-6.33.4 pybase64-1.4.3 pycparser-3.0 pydantic-2.12.5 pydantic-core-2.41.5 pydantic-settings-2.12.0 pygments-2.19.2 pyjwt-2.10.1 pylint-4.0.4 pypika-0.50.0 pyproject_hooks-1.2.0 pytest-9.0.2 pytest-cov-7.0.0 python-dateutil-2.9.0.post0 python-dotenv-1.2.1 python-multipart-0.0.22 pytokens-0.4.0 pyyaml-6.0.3 radon-6.0.1 referencing-0.37.0 regex-2026.1.15 requests-2.32.5 requests-oauthlib-2.0.0 requests-toolbelt-1.0.0 rich-14.3.1 rpds-py-0.30.0 ruff-0.14.14 safetensors-0.7.0 scikit-learn-1.7.2 scipy-1.15.3 sentence-transformers-5.2.0 shellingham-1.5.4 six-1.17.0 smmap-5.0.2 sse-starlette-3.2.0 starlette-0.52.1 sympy-1.14.0 tenacity-9.1.2 threadpoolctl-3.6.0 tokenizers-0.22.2 tomli-2.4.0 tomlkit-0.14.0 torch-2.10.0 tqdm-4.67.1 transformers-5.0.0 triton-3.6.0 typer-0.21.1 typer-slim-0.21.1 typing-extensions-4.15.0 typing-inspection-0.4.2 urllib3-2.6.3 uuid-utils-0.14.0 uvicorn-0.40.0 uvloop-0.22.1 virtualenv-20.36.1 watchfiles-1.1.1 websocket-client-1.9.0 websockets-16.0 zipp-3.23.0 zstandard-0.25.0
2026-01-26T14:33:47.3273789Z ##[group]Run ruff check .
2026-01-26T14:33:47.3274063Z [36;1mruff check .[0m
2026-01-26T14:33:47.4008510Z shell: /usr/bin/bash -e {0}
2026-01-26T14:33:47.4009152Z env:
2026-01-26T14:33:47.4009556Z   pythonLocation: /opt/hostedtoolcache/Python/3.10.19/x64
2026-01-26T14:33:47.4010250Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.10.19/x64/lib/pkgconfig
2026-01-26T14:33:47.4010960Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.10.19/x64
2026-01-26T14:33:47.4011581Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.10.19/x64
2026-01-26T14:33:47.4012231Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.10.19/x64
2026-01-26T14:33:47.4012624Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.10.19/x64/lib
2026-01-26T14:33:47.4013048Z ##[endgroup]
2026-01-26T14:33:47.4365649Z warning: The top-level linter settings are deprecated in favour of their counterparts in the `lint` section. Please update the following options in `pyproject.toml`:
2026-01-26T14:33:47.4367287Z   - 'ignore' -> 'lint.ignore'
2026-01-26T14:33:47.4367746Z   - 'select' -> 'lint.select'
2026-01-26T14:33:47.4728093Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.4730641Z  --> cache_manager.py:1:1
2026-01-26T14:33:47.4731017Z   |
2026-01-26T14:33:47.4731269Z 1 | / import time
2026-01-26T14:33:47.4731657Z 2 | | from typing import Any, Optional, Dict, Tuple
2026-01-26T14:33:47.4732163Z 3 | | from collections import OrderedDict
2026-01-26T14:33:47.4732623Z 4 | | from threading import Lock
2026-01-26T14:33:47.4733026Z 5 | | from pathlib import Path
2026-01-26T14:33:47.4733370Z 6 | |
2026-01-26T14:33:47.4733659Z 7 | | from logger import get_logger
2026-01-26T14:33:47.4734042Z   | |_____________________________^
2026-01-26T14:33:47.4734424Z 8 |
2026-01-26T14:33:47.4734685Z 9 |   logger = get_logger()
2026-01-26T14:33:47.4735013Z   |
2026-01-26T14:33:47.4735271Z help: Organize imports
2026-01-26T14:33:47.4735490Z 
2026-01-26T14:33:47.4735711Z UP035 `typing.Dict` is deprecated, use `dict` instead
2026-01-26T14:33:47.4736229Z  --> cache_manager.py:2:1
2026-01-26T14:33:47.4736561Z   |
2026-01-26T14:33:47.4736815Z 1 | import time
2026-01-26T14:33:47.4737185Z 2 | from typing import Any, Optional, Dict, Tuple
2026-01-26T14:33:47.4737633Z   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.4738074Z 3 | from collections import OrderedDict
2026-01-26T14:33:47.4738562Z 4 | from threading import Lock
2026-01-26T14:33:47.4739178Z   |
2026-01-26T14:33:47.4739335Z 
2026-01-26T14:33:47.4739564Z UP035 `typing.Tuple` is deprecated, use `tuple` instead
2026-01-26T14:33:47.4740030Z  --> cache_manager.py:2:1
2026-01-26T14:33:47.4740330Z   |
2026-01-26T14:33:47.4740578Z 1 | import time
2026-01-26T14:33:47.4740898Z 2 | from typing import Any, Optional, Dict, Tuple
2026-01-26T14:33:47.4741332Z   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.4741726Z 3 | from collections import OrderedDict
2026-01-26T14:33:47.4742156Z 4 | from threading import Lock
2026-01-26T14:33:47.4742506Z   |
2026-01-26T14:33:47.4742669Z 
2026-01-26T14:33:47.4742818Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4743245Z   --> cache_manager.py:17:1
2026-01-26T14:33:47.4743577Z    |
2026-01-26T14:33:47.4744059Z 15 |     Automatically evicts least recently used items when capacity is reached.
2026-01-26T14:33:47.4744667Z 16 |     """
2026-01-26T14:33:47.4744927Z 17 |     
2026-01-26T14:33:47.4745173Z    | ^^^^
2026-01-26T14:33:47.4745495Z 18 |     def __init__(self, capacity: int = 100):
2026-01-26T14:33:47.4745921Z 19 |         """
2026-01-26T14:33:47.4746195Z    |
2026-01-26T14:33:47.4746480Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4746785Z 
2026-01-26T14:33:47.4746928Z W293 Blank line contains whitespace
2026-01-26T14:33:47.4747623Z   --> cache_manager.py:21:1
2026-01-26T14:33:47.4747959Z    |
2026-01-26T14:33:47.4748204Z 19 |         """
2026-01-26T14:33:47.4748500Z 20 |         Initialize LRU cache.
2026-01-26T14:33:47.4749070Z 21 |         
2026-01-26T14:33:47.4749336Z    | ^^^^^^^^
2026-01-26T14:33:47.4749859Z 22 |         Args:
2026-01-26T14:33:47.4750239Z 23 |             capacity: Maximum number of items to cache
2026-01-26T14:33:47.4750780Z    |
2026-01-26T14:33:47.4751122Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4751419Z 
2026-01-26T14:33:47.4751572Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4751993Z   --> cache_manager.py:30:1
2026-01-26T14:33:47.4752311Z    |
2026-01-26T14:33:47.4752566Z 28 |         self.hits = 0
2026-01-26T14:33:47.4752903Z 29 |         self.misses = 0
2026-01-26T14:33:47.4753238Z 30 |     
2026-01-26T14:33:47.4753491Z    | ^^^^
2026-01-26T14:33:47.4753831Z 31 |     def get(self, key: str) -> Optional[Any]:
2026-01-26T14:33:47.4754288Z 32 |         """
2026-01-26T14:33:47.4754568Z    |
2026-01-26T14:33:47.4754867Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4755157Z 
2026-01-26T14:33:47.4755324Z UP045 [*] Use `X | None` for type annotations
2026-01-26T14:33:47.4755769Z   --> cache_manager.py:31:32
2026-01-26T14:33:47.4756133Z    |
2026-01-26T14:33:47.4756389Z 29 |         self.misses = 0
2026-01-26T14:33:47.4756722Z 30 |     
2026-01-26T14:33:47.4757043Z 31 |     def get(self, key: str) -> Optional[Any]:
2026-01-26T14:33:47.4757505Z    |                                ^^^^^^^^^^^^^
2026-01-26T14:33:47.4757891Z 32 |         """
2026-01-26T14:33:47.4758212Z 33 |         Retrieves value from cache.
2026-01-26T14:33:47.4758595Z    |
2026-01-26T14:33:47.4759074Z help: Convert to `X | None`
2026-01-26T14:33:47.4759314Z 
2026-01-26T14:33:47.4759483Z W293 Blank line contains whitespace
2026-01-26T14:33:47.4759888Z   --> cache_manager.py:34:1
2026-01-26T14:33:47.4760220Z    |
2026-01-26T14:33:47.4760460Z 32 |         """
2026-01-26T14:33:47.4760774Z 33 |         Retrieves value from cache.
2026-01-26T14:33:47.4761173Z 34 |         
2026-01-26T14:33:47.4761433Z    | ^^^^^^^^
2026-01-26T14:33:47.4761697Z 35 |         Args:
2026-01-26T14:33:47.4761993Z 36 |             key: Cache key
2026-01-26T14:33:47.4762321Z    |
2026-01-26T14:33:47.4762619Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4762916Z 
2026-01-26T14:33:47.4763071Z W293 Blank line contains whitespace
2026-01-26T14:33:47.4763468Z   --> cache_manager.py:37:1
2026-01-26T14:33:47.4763797Z    |
2026-01-26T14:33:47.4764040Z 35 |         Args:
2026-01-26T14:33:47.4764344Z 36 |             key: Cache key
2026-01-26T14:33:47.4764671Z 37 |             
2026-01-26T14:33:47.4764947Z    | ^^^^^^^^^^^^
2026-01-26T14:33:47.4765220Z 38 |         Returns:
2026-01-26T14:33:47.4765587Z 39 |             Cached value or None if not found
2026-01-26T14:33:47.4765999Z    |
2026-01-26T14:33:47.4766289Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4766587Z 
2026-01-26T14:33:47.4766744Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4767178Z   --> cache_manager.py:48:1
2026-01-26T14:33:47.4767506Z    |
2026-01-26T14:33:47.4767828Z 46 |             self.misses += 1
2026-01-26T14:33:47.4768224Z 47 |             return None
2026-01-26T14:33:47.4768550Z 48 |     
2026-01-26T14:33:47.4768939Z    | ^^^^
2026-01-26T14:33:47.4769278Z 49 |     def put(self, key: str, value: Any) -> None:
2026-01-26T14:33:47.4769725Z 50 |         """
2026-01-26T14:33:47.4769991Z    |
2026-01-26T14:33:47.4770284Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4770569Z 
2026-01-26T14:33:47.4770712Z W293 Blank line contains whitespace
2026-01-26T14:33:47.4771095Z   --> cache_manager.py:52:1
2026-01-26T14:33:47.4771415Z    |
2026-01-26T14:33:47.4771650Z 50 |         """
2026-01-26T14:33:47.4771975Z 51 |         Adds or updates value in cache.
2026-01-26T14:33:47.4772368Z 52 |         
2026-01-26T14:33:47.4772632Z    | ^^^^^^^^
2026-01-26T14:33:47.4772891Z 53 |         Args:
2026-01-26T14:33:47.4773435Z 54 |             key: Cache key
2026-01-26T14:33:47.4773769Z    |
2026-01-26T14:33:47.4774047Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4774332Z 
2026-01-26T14:33:47.4774481Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4775087Z   --> cache_manager.py:66:1
2026-01-26T14:33:47.4775448Z    |
2026-01-26T14:33:47.4775819Z 64 |                     logger.debug(f"LRU cache evicted: {oldest_key}")
2026-01-26T14:33:47.4776364Z 65 |             self.cache[key] = value
2026-01-26T14:33:47.4776743Z 66 |     
2026-01-26T14:33:47.4776994Z    | ^^^^
2026-01-26T14:33:47.4777273Z 67 |     def clear(self) -> None:
2026-01-26T14:33:47.4777689Z 68 |         """Clears all cached items."""
2026-01-26T14:33:47.4778096Z    |
2026-01-26T14:33:47.4778392Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4778694Z 
2026-01-26T14:33:47.4779018Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4779443Z   --> cache_manager.py:72:1
2026-01-26T14:33:47.4779783Z    |
2026-01-26T14:33:47.4780058Z 70 |             self.cache.clear()
2026-01-26T14:33:47.4780491Z 71 |             logger.debug("LRU cache cleared")
2026-01-26T14:33:47.4780917Z 72 |     
2026-01-26T14:33:47.4781168Z    | ^^^^
2026-01-26T14:33:47.4781478Z 73 |     def get_stats(self) -> Dict[str, Any]:
2026-01-26T14:33:47.4781889Z 74 |         """
2026-01-26T14:33:47.4782154Z    |
2026-01-26T14:33:47.4782434Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4782723Z 
2026-01-26T14:33:47.4782944Z UP006 [*] Use `dict` instead of `Dict` for type annotation
2026-01-26T14:33:47.4783429Z   --> cache_manager.py:73:28
2026-01-26T14:33:47.4783779Z    |
2026-01-26T14:33:47.4784081Z 71 |             logger.debug("LRU cache cleared")
2026-01-26T14:33:47.4784510Z 72 |     
2026-01-26T14:33:47.4784818Z 73 |     def get_stats(self) -> Dict[str, Any]:
2026-01-26T14:33:47.4785228Z    |                            ^^^^
2026-01-26T14:33:47.4785588Z 74 |         """
2026-01-26T14:33:47.4785888Z 75 |         Returns cache statistics.
2026-01-26T14:33:47.4786262Z    |
2026-01-26T14:33:47.4786530Z help: Replace with `dict`
2026-01-26T14:33:47.4786771Z 
2026-01-26T14:33:47.4786908Z W293 Blank line contains whitespace
2026-01-26T14:33:47.4787311Z   --> cache_manager.py:76:1
2026-01-26T14:33:47.4787633Z    |
2026-01-26T14:33:47.4787871Z 74 |         """
2026-01-26T14:33:47.4788179Z 75 |         Returns cache statistics.
2026-01-26T14:33:47.4788556Z 76 |         
2026-01-26T14:33:47.4788968Z    | ^^^^^^^^
2026-01-26T14:33:47.4789245Z 77 |         Returns:
2026-01-26T14:33:47.4789676Z 78 |             Dictionary with hits, misses, size, capacity, hit_rate
2026-01-26T14:33:47.4790185Z    |
2026-01-26T14:33:47.4790466Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4790768Z 
2026-01-26T14:33:47.4790914Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4791321Z   --> cache_manager.py:97:1
2026-01-26T14:33:47.4791653Z    |
2026-01-26T14:33:47.4792019Z 95 |     Items are automatically removed after specified TTL.
2026-01-26T14:33:47.4792505Z 96 |     """
2026-01-26T14:33:47.4792767Z 97 |     
2026-01-26T14:33:47.4793009Z    | ^^^^
2026-01-26T14:33:47.4793415Z 98 |     def __init__(self, ttl_seconds: int = 300, max_size: int = 100):
2026-01-26T14:33:47.4793938Z 99 |         """
2026-01-26T14:33:47.4794216Z    |
2026-01-26T14:33:47.4794503Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4794805Z 
2026-01-26T14:33:47.4794949Z W293 Blank line contains whitespace
2026-01-26T14:33:47.4795355Z    --> cache_manager.py:101:1
2026-01-26T14:33:47.4795704Z     |
2026-01-26T14:33:47.4795951Z  99 |         """
2026-01-26T14:33:47.4796248Z 100 |         Initialize TTL cache.
2026-01-26T14:33:47.4796648Z 101 |         
2026-01-26T14:33:47.4796919Z     | ^^^^^^^^
2026-01-26T14:33:47.4797181Z 102 |         Args:
2026-01-26T14:33:47.4797600Z 103 |             ttl_seconds: Time to live for cached items in seconds
2026-01-26T14:33:47.4798095Z     |
2026-01-26T14:33:47.4798391Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4799077Z 
2026-01-26T14:33:47.4799314Z UP006 [*] Use `dict` instead of `Dict` for type annotation
2026-01-26T14:33:47.4799830Z    --> cache_manager.py:108:21
2026-01-26T14:33:47.4800172Z     |
2026-01-26T14:33:47.4800461Z 106 |         self.ttl_seconds = ttl_seconds
2026-01-26T14:33:47.4801084Z 107 |         self.max_size = max_size
2026-01-26T14:33:47.4801580Z 108 |         self.cache: Dict[str, Tuple[Any, float]] = {}
2026-01-26T14:33:47.4802045Z     |                     ^^^^
2026-01-26T14:33:47.4802381Z 109 |         self.lock = Lock()
2026-01-26T14:33:47.4802742Z 110 |         self.hits = 0
2026-01-26T14:33:47.4803064Z     |
2026-01-26T14:33:47.4803332Z help: Replace with `dict`
2026-01-26T14:33:47.4803559Z 
2026-01-26T14:33:47.4803790Z UP006 [*] Use `tuple` instead of `Tuple` for type annotation
2026-01-26T14:33:47.4804301Z    --> cache_manager.py:108:31
2026-01-26T14:33:47.4804647Z     |
2026-01-26T14:33:47.4804934Z 106 |         self.ttl_seconds = ttl_seconds
2026-01-26T14:33:47.4805368Z 107 |         self.max_size = max_size
2026-01-26T14:33:47.4805848Z 108 |         self.cache: Dict[str, Tuple[Any, float]] = {}
2026-01-26T14:33:47.4806331Z     |                               ^^^^^
2026-01-26T14:33:47.4806727Z 109 |         self.lock = Lock()
2026-01-26T14:33:47.4807095Z 110 |         self.hits = 0
2026-01-26T14:33:47.4807417Z     |
2026-01-26T14:33:47.4807685Z help: Replace with `tuple`
2026-01-26T14:33:47.4807922Z 
2026-01-26T14:33:47.4808079Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4808500Z    --> cache_manager.py:113:1
2026-01-26T14:33:47.4808996Z     |
2026-01-26T14:33:47.4809252Z 111 |         self.misses = 0
2026-01-26T14:33:47.4809611Z 112 |         self.expirations = 0
2026-01-26T14:33:47.4809971Z 113 |     
2026-01-26T14:33:47.4810227Z     | ^^^^
2026-01-26T14:33:47.4810560Z 114 |     def get(self, key: str) -> Optional[Any]:
2026-01-26T14:33:47.4810988Z 115 |         """
2026-01-26T14:33:47.4811265Z     |
2026-01-26T14:33:47.4811555Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4811870Z 
2026-01-26T14:33:47.4812034Z UP045 [*] Use `X | None` for type annotations
2026-01-26T14:33:47.4812475Z    --> cache_manager.py:114:32
2026-01-26T14:33:47.4812824Z     |
2026-01-26T14:33:47.4813090Z 112 |         self.expirations = 0
2026-01-26T14:33:47.4813462Z 113 |     
2026-01-26T14:33:47.4813790Z 114 |     def get(self, key: str) -> Optional[Any]:
2026-01-26T14:33:47.4814249Z     |                                ^^^^^^^^^^^^^
2026-01-26T14:33:47.4814641Z 115 |         """
2026-01-26T14:33:47.4814999Z 116 |         Retrieves value from cache if not expired.
2026-01-26T14:33:47.4815442Z     |
2026-01-26T14:33:47.4815717Z help: Convert to `X | None`
2026-01-26T14:33:47.4815954Z 
2026-01-26T14:33:47.4816093Z W293 Blank line contains whitespace
2026-01-26T14:33:47.4816483Z    --> cache_manager.py:117:1
2026-01-26T14:33:47.4816819Z     |
2026-01-26T14:33:47.4817069Z 115 |         """
2026-01-26T14:33:47.4817429Z 116 |         Retrieves value from cache if not expired.
2026-01-26T14:33:47.4817886Z 117 |         
2026-01-26T14:33:47.4818149Z     | ^^^^^^^^
2026-01-26T14:33:47.4818417Z 118 |         Args:
2026-01-26T14:33:47.4818713Z 119 |             key: Cache key
2026-01-26T14:33:47.4819220Z     |
2026-01-26T14:33:47.4819518Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4819819Z 
2026-01-26T14:33:47.4819962Z W293 Blank line contains whitespace
2026-01-26T14:33:47.4820360Z    --> cache_manager.py:120:1
2026-01-26T14:33:47.4820721Z     |
2026-01-26T14:33:47.4820970Z 118 |         Args:
2026-01-26T14:33:47.4821266Z 119 |             key: Cache key
2026-01-26T14:33:47.4821608Z 120 |             
2026-01-26T14:33:47.4821879Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.4822162Z 121 |         Returns:
2026-01-26T14:33:47.4822555Z 122 |             Cached value or None if not found or expired
2026-01-26T14:33:47.4823019Z     |
2026-01-26T14:33:47.4823306Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4823604Z 
2026-01-26T14:33:47.4823750Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4824381Z    --> cache_manager.py:136:1
2026-01-26T14:33:47.4824721Z     |
2026-01-26T14:33:47.4824989Z 134 |             self.misses += 1
2026-01-26T14:33:47.4825353Z 135 |             return None
2026-01-26T14:33:47.4825685Z 136 |     
2026-01-26T14:33:47.4826095Z     | ^^^^
2026-01-26T14:33:47.4826458Z 137 |     def put(self, key: str, value: Any) -> None:
2026-01-26T14:33:47.4826903Z 138 |         """
2026-01-26T14:33:47.4827176Z     |
2026-01-26T14:33:47.4827462Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4827762Z 
2026-01-26T14:33:47.4827903Z W293 Blank line contains whitespace
2026-01-26T14:33:47.4828305Z    --> cache_manager.py:140:1
2026-01-26T14:33:47.4828639Z     |
2026-01-26T14:33:47.4829037Z 138 |         """
2026-01-26T14:33:47.4829459Z 139 |         Adds or updates value in cache with current timestamp.
2026-01-26T14:33:47.4829970Z 140 |         
2026-01-26T14:33:47.4830235Z     | ^^^^^^^^
2026-01-26T14:33:47.4830504Z 141 |         Args:
2026-01-26T14:33:47.4830808Z 142 |             key: Cache key
2026-01-26T14:33:47.4831151Z     |
2026-01-26T14:33:47.4831438Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4831740Z 
2026-01-26T14:33:47.4831883Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4832307Z    --> cache_manager.py:148:1
2026-01-26T14:33:47.4832645Z     |
2026-01-26T14:33:47.4833061Z 146 |             if len(self.cache) >= self.max_size and key not in self.cache:
2026-01-26T14:33:47.4833642Z 147 |                 self._evict_oldest()
2026-01-26T14:33:47.4834034Z 148 |             
2026-01-26T14:33:47.4834305Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.4834658Z 149 |             self.cache[key] = (value, time.time())
2026-01-26T14:33:47.4835086Z     |
2026-01-26T14:33:47.4835379Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4835668Z 
2026-01-26T14:33:47.4835816Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4836224Z    --> cache_manager.py:150:1
2026-01-26T14:33:47.4836566Z     |
2026-01-26T14:33:47.4836887Z 149 |             self.cache[key] = (value, time.time())
2026-01-26T14:33:47.4837318Z 150 |     
2026-01-26T14:33:47.4837568Z     | ^^^^
2026-01-26T14:33:47.4837864Z 151 |     def _evict_oldest(self) -> None:
2026-01-26T14:33:47.4838335Z 152 |         """Evicts the oldest item from cache."""
2026-01-26T14:33:47.4838760Z     |
2026-01-26T14:33:47.4839215Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4839514Z 
2026-01-26T14:33:47.4840548Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4840963Z    --> cache_manager.py:155:1
2026-01-26T14:33:47.4841305Z     |
2026-01-26T14:33:47.4841558Z 153 |         if not self.cache:
2026-01-26T14:33:47.4841886Z 154 |             return
2026-01-26T14:33:47.4842167Z 155 |         
2026-01-26T14:33:47.4842407Z     | ^^^^^^^^
2026-01-26T14:33:47.4842804Z 156 |         oldest_key = min(self.cache.items(), key=lambda x: x[1][1])[0]
2026-01-26T14:33:47.4843296Z 157 |         del self.cache[oldest_key]
2026-01-26T14:33:47.4843644Z     |
2026-01-26T14:33:47.4843924Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4844180Z 
2026-01-26T14:33:47.4844319Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4844773Z    --> cache_manager.py:159:1
2026-01-26T14:33:47.4845126Z     |
2026-01-26T14:33:47.4845419Z 157 |         del self.cache[oldest_key]
2026-01-26T14:33:47.4845908Z 158 |         logger.debug(f"TTL cache evicted oldest: {oldest_key}")
2026-01-26T14:33:47.4846345Z 159 |     
2026-01-26T14:33:47.4846576Z     | ^^^^
2026-01-26T14:33:47.4846839Z 160 |     def clear(self) -> None:
2026-01-26T14:33:47.4847222Z 161 |         """Clears all cached items."""
2026-01-26T14:33:47.4847616Z     |
2026-01-26T14:33:47.4847900Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4848193Z 
2026-01-26T14:33:47.4848347Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4848954Z    --> cache_manager.py:165:1
2026-01-26T14:33:47.4849328Z     |
2026-01-26T14:33:47.4849604Z 163 |             self.cache.clear()
2026-01-26T14:33:47.4850264Z 164 |             logger.debug("TTL cache cleared")
2026-01-26T14:33:47.4850681Z 165 |     
2026-01-26T14:33:47.4850940Z     | ^^^^
2026-01-26T14:33:47.4851254Z 166 |     def cleanup_expired(self) -> int:
2026-01-26T14:33:47.4851659Z 167 |         """
2026-01-26T14:33:47.4852103Z     |
2026-01-26T14:33:47.4852404Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4852701Z 
2026-01-26T14:33:47.4852852Z W293 Blank line contains whitespace
2026-01-26T14:33:47.4853257Z    --> cache_manager.py:169:1
2026-01-26T14:33:47.4853604Z     |
2026-01-26T14:33:47.4853846Z 167 |         """
2026-01-26T14:33:47.4854193Z 168 |         Removes all expired items from cache.
2026-01-26T14:33:47.4854619Z 169 |         
2026-01-26T14:33:47.4854886Z     | ^^^^^^^^
2026-01-26T14:33:47.4855163Z 170 |         Returns:
2026-01-26T14:33:47.4855496Z 171 |             Number of items removed
2026-01-26T14:33:47.4855890Z     |
2026-01-26T14:33:47.4856181Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4856481Z 
2026-01-26T14:33:47.4856635Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4857035Z    --> cache_manager.py:179:1
2026-01-26T14:33:47.4857372Z     |
2026-01-26T14:33:47.4857730Z 177 |                 if current_time - timestamp >= self.ttl_seconds
2026-01-26T14:33:47.4858230Z 178 |             ]
2026-01-26T14:33:47.4858510Z 179 |             
2026-01-26T14:33:47.4858946Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.4859275Z 180 |             for key in expired_keys:
2026-01-26T14:33:47.4859699Z 181 |                 del self.cache[key]
2026-01-26T14:33:47.4860081Z     |
2026-01-26T14:33:47.4860367Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4860664Z 
2026-01-26T14:33:47.4860807Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4861214Z    --> cache_manager.py:183:1
2026-01-26T14:33:47.4861560Z     |
2026-01-26T14:33:47.4861842Z 181 |                 del self.cache[key]
2026-01-26T14:33:47.4862267Z 182 |                 self.expirations += 1
2026-01-26T14:33:47.4862666Z 183 |             
2026-01-26T14:33:47.4862945Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.4863253Z 184 |             if expired_keys:
2026-01-26T14:33:47.4863889Z 185 |                 logger.debug(f"TTL cache cleanup: removed {len(expired_keys)} expired items")
2026-01-26T14:33:47.4864534Z     |
2026-01-26T14:33:47.4864815Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4865111Z 
2026-01-26T14:33:47.4865258Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4865681Z    --> cache_manager.py:186:1
2026-01-26T14:33:47.4866021Z     |
2026-01-26T14:33:47.4866296Z 184 |             if expired_keys:
2026-01-26T14:33:47.4866915Z 185 |                 logger.debug(f"TTL cache cleanup: removed {len(expired_keys)} expired items")
2026-01-26T14:33:47.4867624Z 186 |             
2026-01-26T14:33:47.4867974Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.4868299Z 187 |             return len(expired_keys)
2026-01-26T14:33:47.4868681Z     |
2026-01-26T14:33:47.4869130Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4869432Z 
2026-01-26T14:33:47.4869579Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4869990Z    --> cache_manager.py:188:1
2026-01-26T14:33:47.4870337Z     |
2026-01-26T14:33:47.4870623Z 187 |             return len(expired_keys)
2026-01-26T14:33:47.4871021Z 188 |     
2026-01-26T14:33:47.4871276Z     | ^^^^
2026-01-26T14:33:47.4871594Z 189 |     def get_stats(self) -> Dict[str, Any]:
2026-01-26T14:33:47.4872000Z 190 |         """
2026-01-26T14:33:47.4872274Z     |
2026-01-26T14:33:47.4872556Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4872842Z 
2026-01-26T14:33:47.4873053Z UP006 [*] Use `dict` instead of `Dict` for type annotation
2026-01-26T14:33:47.4873552Z    --> cache_manager.py:189:28
2026-01-26T14:33:47.4873884Z     |
2026-01-26T14:33:47.4874162Z 187 |             return len(expired_keys)
2026-01-26T14:33:47.4874544Z 188 |     
2026-01-26T14:33:47.4874850Z 189 |     def get_stats(self) -> Dict[str, Any]:
2026-01-26T14:33:47.4875270Z     |                            ^^^^
2026-01-26T14:33:47.4875935Z 190 |         """
2026-01-26T14:33:47.4876247Z 191 |         Returns cache statistics.
2026-01-26T14:33:47.4876629Z     |
2026-01-26T14:33:47.4876908Z help: Replace with `dict`
2026-01-26T14:33:47.4877136Z 
2026-01-26T14:33:47.4877437Z W293 Blank line contains whitespace
2026-01-26T14:33:47.4877861Z    --> cache_manager.py:192:1
2026-01-26T14:33:47.4878208Z     |
2026-01-26T14:33:47.4878458Z 190 |         """
2026-01-26T14:33:47.4878930Z 191 |         Returns cache statistics.
2026-01-26T14:33:47.4879331Z 192 |         
2026-01-26T14:33:47.4879596Z     | ^^^^^^^^
2026-01-26T14:33:47.4879873Z 193 |         Returns:
2026-01-26T14:33:47.4880337Z 194 |             Dictionary with hits, misses, size, expirations, hit_rate
2026-01-26T14:33:47.4880884Z     |
2026-01-26T14:33:47.4881183Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4881478Z 
2026-01-26T14:33:47.4881621Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4882044Z    --> cache_manager.py:215:1
2026-01-26T14:33:47.4882394Z     |
2026-01-26T14:33:47.4882788Z 213 |     Automatically invalidates cache when file is modified.
2026-01-26T14:33:47.4883300Z 214 |     """
2026-01-26T14:33:47.4883572Z 215 |     
2026-01-26T14:33:47.4883820Z     | ^^^^
2026-01-26T14:33:47.4884142Z 216 |     def __init__(self, capacity: int = 50):
2026-01-26T14:33:47.4884569Z 217 |         """
2026-01-26T14:33:47.4884835Z     |
2026-01-26T14:33:47.4885126Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4885420Z 
2026-01-26T14:33:47.4885565Z W293 Blank line contains whitespace
2026-01-26T14:33:47.4885974Z    --> cache_manager.py:219:1
2026-01-26T14:33:47.4886312Z     |
2026-01-26T14:33:47.4886557Z 217 |         """
2026-01-26T14:33:47.4886854Z 218 |         Initialize file cache.
2026-01-26T14:33:47.4887228Z 219 |         
2026-01-26T14:33:47.4887489Z     | ^^^^^^^^
2026-01-26T14:33:47.4887759Z 220 |         Args:
2026-01-26T14:33:47.4888139Z 221 |             capacity: Maximum number of files to cache
2026-01-26T14:33:47.4888595Z     |
2026-01-26T14:33:47.4889038Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4889338Z 
2026-01-26T14:33:47.4889553Z UP006 [*] Use `dict` instead of `Dict` for type annotation
2026-01-26T14:33:47.4890069Z    --> cache_manager.py:224:27
2026-01-26T14:33:47.4890420Z     |
2026-01-26T14:33:47.4890662Z 222 |         """
2026-01-26T14:33:47.4890978Z 223 |         self.lru_cache = LRUCache(capacity)
2026-01-26T14:33:47.4891464Z 224 |         self.mtime_cache: Dict[str, float] = {}
2026-01-26T14:33:47.4891902Z     |                           ^^^^
2026-01-26T14:33:47.4892268Z 225 |         self.lock = Lock()
2026-01-26T14:33:47.4892612Z     |
2026-01-26T14:33:47.4892890Z help: Replace with `dict`
2026-01-26T14:33:47.4893122Z 
2026-01-26T14:33:47.4893281Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4893711Z    --> cache_manager.py:226:1
2026-01-26T14:33:47.4894117Z     |
2026-01-26T14:33:47.4894438Z 224 |         self.mtime_cache: Dict[str, float] = {}
2026-01-26T14:33:47.4894901Z 225 |         self.lock = Lock()
2026-01-26T14:33:47.4895254Z 226 |     
2026-01-26T14:33:47.4895501Z     | ^^^^
2026-01-26T14:33:47.4895872Z 227 |     def get(self, file_path: Path) -> Optional[str]:
2026-01-26T14:33:47.4896345Z 228 |         """
2026-01-26T14:33:47.4896617Z     |
2026-01-26T14:33:47.4896898Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4897188Z 
2026-01-26T14:33:47.4897349Z UP045 [*] Use `X | None` for type annotations
2026-01-26T14:33:47.4897785Z    --> cache_manager.py:227:39
2026-01-26T14:33:47.4898133Z     |
2026-01-26T14:33:47.4898401Z 225 |         self.lock = Lock()
2026-01-26T14:33:47.4898739Z 226 |     
2026-01-26T14:33:47.4899262Z 227 |     def get(self, file_path: Path) -> Optional[str]:
2026-01-26T14:33:47.4899768Z     |                                       ^^^^^^^^^^^^^
2026-01-26T14:33:47.4900175Z 228 |         """
2026-01-26T14:33:47.4900647Z 229 |         Retrieves file content from cache if file hasn't been modified.
2026-01-26T14:33:47.4901420Z     |
2026-01-26T14:33:47.4901692Z help: Convert to `X | None`
2026-01-26T14:33:47.4901933Z 
2026-01-26T14:33:47.4902077Z W293 Blank line contains whitespace
2026-01-26T14:33:47.4902485Z    --> cache_manager.py:230:1
2026-01-26T14:33:47.4902827Z     |
2026-01-26T14:33:47.4903242Z 228 |         """
2026-01-26T14:33:47.4903720Z 229 |         Retrieves file content from cache if file hasn't been modified.
2026-01-26T14:33:47.4904294Z 230 |         
2026-01-26T14:33:47.4904553Z     | ^^^^^^^^
2026-01-26T14:33:47.4904835Z 231 |         Args:
2026-01-26T14:33:47.4905146Z 232 |             file_path: Path to file
2026-01-26T14:33:47.4905538Z     |
2026-01-26T14:33:47.4905832Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4906135Z 
2026-01-26T14:33:47.4906278Z W293 Blank line contains whitespace
2026-01-26T14:33:47.4906686Z    --> cache_manager.py:233:1
2026-01-26T14:33:47.4907024Z     |
2026-01-26T14:33:47.4907269Z 231 |         Args:
2026-01-26T14:33:47.4907583Z 232 |             file_path: Path to file
2026-01-26T14:33:47.4907980Z 233 |             
2026-01-26T14:33:47.4908252Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.4908536Z 234 |         Returns:
2026-01-26T14:33:47.4909131Z 235 |             Cached file content or None if not cached or modified
2026-01-26T14:33:47.4909654Z     |
2026-01-26T14:33:47.4909949Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4910237Z 
2026-01-26T14:33:47.4910382Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4910797Z    --> cache_manager.py:240:1
2026-01-26T14:33:47.4911137Z     |
2026-01-26T14:33:47.4911415Z 238 |             key = str(file_path)
2026-01-26T14:33:47.4911864Z 239 |             current_mtime = file_path.stat().st_mtime
2026-01-26T14:33:47.4912307Z 240 |             
2026-01-26T14:33:47.4912577Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.4912868Z 241 |             with self.lock:
2026-01-26T14:33:47.4913300Z 242 |                 cached_mtime = self.mtime_cache.get(key)
2026-01-26T14:33:47.4913741Z     |
2026-01-26T14:33:47.4914032Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4914311Z 
2026-01-26T14:33:47.4914458Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4914857Z    --> cache_manager.py:243:1
2026-01-26T14:33:47.4915182Z     |
2026-01-26T14:33:47.4915452Z 241 |             with self.lock:
2026-01-26T14:33:47.4915874Z 242 |                 cached_mtime = self.mtime_cache.get(key)
2026-01-26T14:33:47.4916322Z 243 |                 
2026-01-26T14:33:47.4916613Z     | ^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.4917070Z 244 |                 if cached_mtime is not None and cached_mtime == current_mtime:
2026-01-26T14:33:47.4917701Z 245 |                     content = self.lru_cache.get(key)
2026-01-26T14:33:47.4918124Z     |
2026-01-26T14:33:47.4918410Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4918700Z 
2026-01-26T14:33:47.4918994Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4919425Z    --> cache_manager.py:248:1
2026-01-26T14:33:47.4919769Z     |
2026-01-26T14:33:47.4920080Z 246 |                     if content is not None:
2026-01-26T14:33:47.4920530Z 247 |                         return content
2026-01-26T14:33:47.4920916Z 248 |                 
2026-01-26T14:33:47.4921215Z     | ^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.4921525Z 249 |                 return None
2026-01-26T14:33:47.4921908Z 250 |         except Exception as e:
2026-01-26T14:33:47.4922274Z     |
2026-01-26T14:33:47.4922564Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4922859Z 
2026-01-26T14:33:47.4923003Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4923418Z    --> cache_manager.py:253:1
2026-01-26T14:33:47.4923766Z     |
2026-01-26T14:33:47.4924208Z 251 |             logger.debug(f"Error checking file cache for {file_path}: {e}")
2026-01-26T14:33:47.4924810Z 252 |             return None
2026-01-26T14:33:47.4925143Z 253 |     
2026-01-26T14:33:47.4925400Z     | ^^^^
2026-01-26T14:33:47.4925775Z 254 |     def put(self, file_path: Path, content: str) -> None:
2026-01-26T14:33:47.4926461Z 255 |         """
2026-01-26T14:33:47.4926728Z     |
2026-01-26T14:33:47.4927019Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4927310Z 
2026-01-26T14:33:47.4927460Z W293 Blank line contains whitespace
2026-01-26T14:33:47.4928037Z    --> cache_manager.py:257:1
2026-01-26T14:33:47.4928391Z     |
2026-01-26T14:33:47.4928631Z 255 |         """
2026-01-26T14:33:47.4929185Z 256 |         Caches file content with its modification time.
2026-01-26T14:33:47.4929659Z 257 |         
2026-01-26T14:33:47.4929935Z     | ^^^^^^^^
2026-01-26T14:33:47.4930217Z 258 |         Args:
2026-01-26T14:33:47.4930592Z 259 |             file_path: Path to file
2026-01-26T14:33:47.4930984Z     |
2026-01-26T14:33:47.4931281Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4931570Z 
2026-01-26T14:33:47.4931722Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4932156Z    --> cache_manager.py:265:1
2026-01-26T14:33:47.4932506Z     |
2026-01-26T14:33:47.4932771Z 263 |             key = str(file_path)
2026-01-26T14:33:47.4933211Z 264 |             mtime = file_path.stat().st_mtime
2026-01-26T14:33:47.4933625Z 265 |             
2026-01-26T14:33:47.4933901Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.4934188Z 266 |             with self.lock:
2026-01-26T14:33:47.4934620Z 267 |                 self.lru_cache.put(key, content)
2026-01-26T14:33:47.4935050Z     |
2026-01-26T14:33:47.4935336Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4935626Z 
2026-01-26T14:33:47.4935780Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4936186Z    --> cache_manager.py:271:1
2026-01-26T14:33:47.4936527Z     |
2026-01-26T14:33:47.4936795Z 269 |         except Exception as e:
2026-01-26T14:33:47.4937312Z 270 |             logger.debug(f"Error caching file {file_path}: {e}")
2026-01-26T14:33:47.4937810Z 271 |     
2026-01-26T14:33:47.4938059Z     | ^^^^
2026-01-26T14:33:47.4938342Z 272 |     def clear(self) -> None:
2026-01-26T14:33:47.4938745Z 273 |         """Clears all cached files."""
2026-01-26T14:33:47.4939298Z     |
2026-01-26T14:33:47.4939593Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4939896Z 
2026-01-26T14:33:47.4940040Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.4940449Z    --> cache_manager.py:277:1
2026-01-26T14:33:47.4940790Z     |
2026-01-26T14:33:47.4941056Z 275 |             self.lru_cache.clear()
2026-01-26T14:33:47.4941472Z 276 |             self.mtime_cache.clear()
2026-01-26T14:33:47.4941850Z 277 |     
2026-01-26T14:33:47.4942086Z     | ^^^^
2026-01-26T14:33:47.4942395Z 278 |     def get_stats(self) -> Dict[str, Any]:
2026-01-26T14:33:47.4942873Z 279 |         """Returns file cache statistics."""
2026-01-26T14:33:47.4943292Z     |
2026-01-26T14:33:47.4943578Z help: Remove whitespace from blank line
2026-01-26T14:33:47.4943875Z 
2026-01-26T14:33:47.4944089Z UP006 [*] Use `dict` instead of `Dict` for type annotation
2026-01-26T14:33:47.4944590Z    --> cache_manager.py:278:28
2026-01-26T14:33:47.4944942Z     |
2026-01-26T14:33:47.4945225Z 276 |             self.mtime_cache.clear()
2026-01-26T14:33:47.4945609Z 277 |     
2026-01-26T14:33:47.4945911Z 278 |     def get_stats(self) -> Dict[str, Any]:
2026-01-26T14:33:47.4946325Z     |                            ^^^^
2026-01-26T14:33:47.4946748Z 279 |         """Returns file cache statistics."""
2026-01-26T14:33:47.4947215Z 280 |         return self.lru_cache.get_stats()
2026-01-26T14:33:47.4947623Z     |
2026-01-26T14:33:47.4947890Z help: Replace with `dict`
2026-01-26T14:33:47.4948122Z 
2026-01-26T14:33:47.4948301Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.4948918Z   --> codebase_indexer.py:1:1
2026-01-26T14:33:47.4949265Z    |
2026-01-26T14:33:47.4949517Z  1 | / import os
2026-01-26T14:33:47.4949822Z  2 | | from pathlib import Path
2026-01-26T14:33:47.4950211Z  3 | | from typing import Set, List
2026-01-26T14:33:47.4950795Z  4 | | from langchain_text_splitters import RecursiveCharacterTextSplitter
2026-01-26T14:33:47.4951390Z  5 | |
2026-01-26T14:33:47.4951661Z  6 | | from config import (
2026-01-26T14:33:47.4952254Z  7 | |     CHUNK_SIZE,
2026-01-26T14:33:47.4952578Z  8 | |     CHUNK_OVERLAP,
2026-01-26T14:33:47.4952904Z  9 | |     BATCH_SIZE,
2026-01-26T14:33:47.4953215Z 10 | |     BINARY_EXTENSIONS,
2026-01-26T14:33:47.4953735Z 11 | |     INDEXABLE_EXTENSIONS,
2026-01-26T14:33:47.4954143Z 12 | |     get_max_file_size_bytes,
2026-01-26T14:33:47.4954528Z 13 | |     get_max_memory_bytes,
2026-01-26T14:33:47.4954902Z 14 | |     get_ignored_dirs,
2026-01-26T14:33:47.4955249Z 15 | |     safe_read_text,
2026-01-26T14:33:47.4955567Z 16 | | )
2026-01-26T14:33:47.4955914Z 17 | | from incremental_indexing import IndexMetadata
2026-01-26T14:33:47.4956505Z 18 | | from memory_limited_indexer import MemoryLimitedIndexer
2026-01-26T14:33:47.4957099Z 19 | | from vector_store_manager import VectorStoreManager
2026-01-26T14:33:47.4957671Z 20 | | from logger import get_logger
2026-01-26T14:33:47.4958199Z    | |_____________________________^
2026-01-26T14:33:47.4958619Z 21 |
2026-01-26T14:33:47.4959137Z 22 |   logger = get_logger()
2026-01-26T14:33:47.4960011Z    |
2026-01-26T14:33:47.4960357Z help: Organize imports
2026-01-26T14:33:47.4960650Z 
2026-01-26T14:33:47.4960958Z UP035 `typing.Set` is deprecated, use `set` instead
2026-01-26T14:33:47.4961533Z  --> codebase_indexer.py:3:1
2026-01-26T14:33:47.4961975Z   |
2026-01-26T14:33:47.4962478Z 1 | import os
2026-01-26T14:33:47.4962851Z 2 | from pathlib import Path
2026-01-26T14:33:47.4963312Z 3 | from typing import Set, List
2026-01-26T14:33:47.4995874Z   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.4996451Z 4 | from langchain_text_splitters import RecursiveCharacterTextSplitter
2026-01-26T14:33:47.4996970Z   |
2026-01-26T14:33:47.4997104Z 
2026-01-26T14:33:47.4997319Z UP035 `typing.List` is deprecated, use `list` instead
2026-01-26T14:33:47.4997823Z  --> codebase_indexer.py:3:1
2026-01-26T14:33:47.4998156Z   |
2026-01-26T14:33:47.4999993Z 1 | import os
2026-01-26T14:33:47.5000293Z 2 | from pathlib import Path
2026-01-26T14:33:47.5000525Z 3 | from typing import Set, List
2026-01-26T14:33:47.5000760Z   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5001084Z 4 | from langchain_text_splitters import RecursiveCharacterTextSplitter
2026-01-26T14:33:47.5001420Z   |
2026-01-26T14:33:47.5001507Z 
2026-01-26T14:33:47.5001658Z F401 [*] `config.get_ignored_dirs` imported but unused
2026-01-26T14:33:47.5001951Z   --> codebase_indexer.py:14:5
2026-01-26T14:33:47.5002164Z    |
2026-01-26T14:33:47.5002322Z 12 |     get_max_file_size_bytes,
2026-01-26T14:33:47.5002544Z 13 |     get_max_memory_bytes,
2026-01-26T14:33:47.5002747Z 14 |     get_ignored_dirs,
2026-01-26T14:33:47.5002944Z    |     ^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5003132Z 15 |     safe_read_text,
2026-01-26T14:33:47.5003308Z 16 | )
2026-01-26T14:33:47.5003454Z    |
2026-01-26T14:33:47.5003654Z help: Remove unused import: `config.get_ignored_dirs`
2026-01-26T14:33:47.5003855Z 
2026-01-26T14:33:47.5003947Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5004185Z   --> codebase_indexer.py:30:1
2026-01-26T14:33:47.5004393Z    |
2026-01-26T14:33:47.5004632Z 28 |     Encapsulates file scanning, chunking, and indexing logic.
2026-01-26T14:33:47.5004930Z 29 |     """
2026-01-26T14:33:47.5005080Z 30 |     
2026-01-26T14:33:47.5005229Z    | ^^^^
2026-01-26T14:33:47.5005454Z 31 |     def __init__(self, vector_store: VectorStoreManager):
2026-01-26T14:33:47.5005731Z 32 |         """
2026-01-26T14:33:47.5005893Z    |
2026-01-26T14:33:47.5006059Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5006227Z 
2026-01-26T14:33:47.5006318Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5006551Z   --> codebase_indexer.py:34:1
2026-01-26T14:33:47.5006752Z    |
2026-01-26T14:33:47.5006894Z 32 |         """
2026-01-26T14:33:47.5007078Z 33 |         Initialize codebase indexer.
2026-01-26T14:33:47.5007306Z 34 |         
2026-01-26T14:33:47.5007454Z    | ^^^^^^^^
2026-01-26T14:33:47.5007610Z 35 |         Args:
2026-01-26T14:33:47.5007868Z 36 |             vector_store: VectorStoreManager instance for storing chunks
2026-01-26T14:33:47.5008407Z    |
2026-01-26T14:33:47.5008569Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5008744Z 
2026-01-26T14:33:47.5009097Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5009366Z   --> codebase_indexer.py:43:1
2026-01-26T14:33:47.5009709Z    |
2026-01-26T14:33:47.5009883Z 41 |             chunk_overlap=CHUNK_OVERLAP
2026-01-26T14:33:47.5010113Z 42 |         )
2026-01-26T14:33:47.5010269Z 43 |     
2026-01-26T14:33:47.5010410Z    | ^^^^
2026-01-26T14:33:47.5010704Z 44 |     def should_index_file(self, file_path: Path, ignore_patterns: Set[str]) -> bool:
2026-01-26T14:33:47.5011062Z 45 |         """
2026-01-26T14:33:47.5011223Z    |
2026-01-26T14:33:47.5011388Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5011555Z 
2026-01-26T14:33:47.5011678Z UP006 [*] Use `set` instead of `Set` for type annotation
2026-01-26T14:33:47.5011958Z   --> codebase_indexer.py:44:67
2026-01-26T14:33:47.5012161Z    |
2026-01-26T14:33:47.5012306Z 42 |         )
2026-01-26T14:33:47.5012460Z 43 |     
2026-01-26T14:33:47.5012748Z 44 |     def should_index_file(self, file_path: Path, ignore_patterns: Set[str]) -> bool:
2026-01-26T14:33:47.5013143Z    |                                                                   ^^^
2026-01-26T14:33:47.5013410Z 45 |         """
2026-01-26T14:33:47.5013605Z 46 |         Determines if a file should be indexed.
2026-01-26T14:33:47.5013856Z    |
2026-01-26T14:33:47.5014007Z help: Replace with `set`
2026-01-26T14:33:47.5014139Z 
2026-01-26T14:33:47.5014224Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5014467Z   --> codebase_indexer.py:47:1
2026-01-26T14:33:47.5014663Z    |
2026-01-26T14:33:47.5014803Z 45 |         """
2026-01-26T14:33:47.5014991Z 46 |         Determines if a file should be indexed.
2026-01-26T14:33:47.5015231Z 47 |         
2026-01-26T14:33:47.5015377Z    | ^^^^^^^^
2026-01-26T14:33:47.5015531Z 48 |         Args:
2026-01-26T14:33:47.5015709Z 49 |             file_path: Path to check
2026-01-26T14:33:47.5015935Z    |
2026-01-26T14:33:47.5016095Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5016262Z 
2026-01-26T14:33:47.5016344Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5016572Z   --> codebase_indexer.py:51:1
2026-01-26T14:33:47.5016764Z    |
2026-01-26T14:33:47.5016928Z 49 |             file_path: Path to check
2026-01-26T14:33:47.5017178Z 50 |             ignore_patterns: Patterns to ignore
2026-01-26T14:33:47.5017419Z 51 |             
2026-01-26T14:33:47.5017576Z    | ^^^^^^^^^^^^
2026-01-26T14:33:47.5017742Z 52 |         Returns:
2026-01-26T14:33:47.5017934Z 53 |             True if file should be indexed
2026-01-26T14:33:47.5018167Z    |
2026-01-26T14:33:47.5018327Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5018492Z 
2026-01-26T14:33:47.5018574Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5019008Z   --> codebase_indexer.py:57:1
2026-01-26T14:33:47.5019235Z    |
2026-01-26T14:33:47.5019426Z 55 |         if file_path.suffix in BINARY_EXTENSIONS:
2026-01-26T14:33:47.5019687Z 56 |             return False
2026-01-26T14:33:47.5019883Z 57 |         
2026-01-26T14:33:47.5020030Z    | ^^^^^^^^
2026-01-26T14:33:47.5020296Z 58 |         if file_path.suffix and file_path.suffix not in INDEXABLE_EXTENSIONS:
2026-01-26T14:33:47.5020641Z 59 |             return False
2026-01-26T14:33:47.5020835Z    |
2026-01-26T14:33:47.5021011Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5021174Z 
2026-01-26T14:33:47.5021262Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5021498Z   --> codebase_indexer.py:60:1
2026-01-26T14:33:47.5021686Z    |
2026-01-26T14:33:47.5021934Z 58 |         if file_path.suffix and file_path.suffix not in INDEXABLE_EXTENSIONS:
2026-01-26T14:33:47.5022262Z 59 |             return False
2026-01-26T14:33:47.5022450Z 60 |         
2026-01-26T14:33:47.5022599Z    | ^^^^^^^^
2026-01-26T14:33:47.5022772Z 61 |         file_str = str(file_path)
2026-01-26T14:33:47.5023022Z 62 |         for pattern in ignore_patterns:
2026-01-26T14:33:47.5023395Z    |
2026-01-26T14:33:47.5023565Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5023725Z 
2026-01-26T14:33:47.5023807Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5024053Z   --> codebase_indexer.py:65:1
2026-01-26T14:33:47.5024345Z    |
2026-01-26T14:33:47.5024523Z 63 |             if pattern in file_str:
2026-01-26T14:33:47.5024750Z 64 |                 return False
2026-01-26T14:33:47.5024943Z 65 |         
2026-01-26T14:33:47.5025085Z    | ^^^^^^^^
2026-01-26T14:33:47.5025236Z 66 |         try:
2026-01-26T14:33:47.5025430Z 67 |             file_size = file_path.stat().st_size
2026-01-26T14:33:47.5025673Z    |
2026-01-26T14:33:47.5025830Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5025998Z 
2026-01-26T14:33:47.5026078Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5026303Z   --> codebase_indexer.py:73:1
2026-01-26T14:33:47.5026494Z    |
2026-01-26T14:33:47.5026640Z 71 |         except Exception:
2026-01-26T14:33:47.5026837Z 72 |             return False
2026-01-26T14:33:47.5027039Z 73 |         
2026-01-26T14:33:47.5027190Z    | ^^^^^^^^
2026-01-26T14:33:47.5027351Z 74 |         return True
2026-01-26T14:33:47.5027528Z    |
2026-01-26T14:33:47.5027701Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5027873Z 
2026-01-26T14:33:47.5027964Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5028214Z   --> codebase_indexer.py:75:1
2026-01-26T14:33:47.5028414Z    |
2026-01-26T14:33:47.5028557Z 74 |         return True
2026-01-26T14:33:47.5028734Z 75 |     
2026-01-26T14:33:47.5029133Z    | ^^^^
2026-01-26T14:33:47.5029409Z 76 |     def scan_indexable_files(
2026-01-26T14:33:47.5029758Z 77 |         self,
2026-01-26T14:33:47.5029928Z    |
2026-01-26T14:33:47.5030096Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5030263Z 
2026-01-26T14:33:47.5030382Z UP006 [*] Use `set` instead of `Set` for type annotation
2026-01-26T14:33:47.5030669Z   --> codebase_indexer.py:79:23
2026-01-26T14:33:47.5030880Z    |
2026-01-26T14:33:47.5031041Z 77 |         self,
2026-01-26T14:33:47.5031214Z 78 |         root_dir: Path,
2026-01-26T14:33:47.5031419Z 79 |         ignored_dirs: Set[str],
2026-01-26T14:33:47.5031646Z    |                       ^^^
2026-01-26T14:33:47.5031859Z 80 |         ignore_patterns: Set[str]
2026-01-26T14:33:47.5032084Z 81 |     ) -> List[Path]:
2026-01-26T14:33:47.5032264Z    |
2026-01-26T14:33:47.5032412Z help: Replace with `set`
2026-01-26T14:33:47.5032541Z 
2026-01-26T14:33:47.5032655Z UP006 [*] Use `set` instead of `Set` for type annotation
2026-01-26T14:33:47.5032934Z   --> codebase_indexer.py:80:26
2026-01-26T14:33:47.5033128Z    |
2026-01-26T14:33:47.5033280Z 78 |         root_dir: Path,
2026-01-26T14:33:47.5033478Z 79 |         ignored_dirs: Set[str],
2026-01-26T14:33:47.5033698Z 80 |         ignore_patterns: Set[str]
2026-01-26T14:33:47.5033910Z    |                          ^^^
2026-01-26T14:33:47.5034110Z 81 |     ) -> List[Path]:
2026-01-26T14:33:47.5034286Z 82 |         """
2026-01-26T14:33:47.5034447Z    |
2026-01-26T14:33:47.5034597Z help: Replace with `set`
2026-01-26T14:33:47.5034718Z 
2026-01-26T14:33:47.5034846Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5035148Z   --> codebase_indexer.py:81:10
2026-01-26T14:33:47.5035345Z    |
2026-01-26T14:33:47.5035499Z 79 |         ignored_dirs: Set[str],
2026-01-26T14:33:47.5035724Z 80 |         ignore_patterns: Set[str]
2026-01-26T14:33:47.5035950Z 81 |     ) -> List[Path]:
2026-01-26T14:33:47.5036128Z    |          ^^^^
2026-01-26T14:33:47.5036293Z 82 |         """
2026-01-26T14:33:47.5036527Z 83 |         Scans directory tree and returns list of indexable files.
2026-01-26T14:33:47.5036820Z    |
2026-01-26T14:33:47.5036975Z help: Replace with `list`
2026-01-26T14:33:47.5037098Z 
2026-01-26T14:33:47.5037180Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5037416Z   --> codebase_indexer.py:84:1
2026-01-26T14:33:47.5037608Z    |
2026-01-26T14:33:47.5037745Z 82 |         """
2026-01-26T14:33:47.5037972Z 83 |         Scans directory tree and returns list of indexable files.
2026-01-26T14:33:47.5038425Z 84 |         
2026-01-26T14:33:47.5038577Z    | ^^^^^^^^
2026-01-26T14:33:47.5038730Z 85 |         Args:
2026-01-26T14:33:47.5039118Z 86 |             root_dir: Root directory to scan
2026-01-26T14:33:47.5039484Z    |
2026-01-26T14:33:47.5039764Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5039930Z 
2026-01-26T14:33:47.5040011Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5040245Z   --> codebase_indexer.py:89:1
2026-01-26T14:33:47.5040437Z    |
2026-01-26T14:33:47.5040611Z 87 |             ignored_dirs: Directories to skip
2026-01-26T14:33:47.5040896Z 88 |             ignore_patterns: File patterns to ignore
2026-01-26T14:33:47.5041148Z 89 |             
2026-01-26T14:33:47.5041307Z    | ^^^^^^^^^^^^
2026-01-26T14:33:47.5041461Z 90 |         Returns:
2026-01-26T14:33:47.5041659Z 91 |             List of indexable file paths
2026-01-26T14:33:47.5041883Z    |
2026-01-26T14:33:47.5042056Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5042225Z 
2026-01-26T14:33:47.5042309Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5042549Z   --> codebase_indexer.py:94:1
2026-01-26T14:33:47.5042745Z    |
2026-01-26T14:33:47.5042877Z 92 |         """
2026-01-26T14:33:47.5043055Z 93 |         indexable_files = []
2026-01-26T14:33:47.5043263Z 94 |         
2026-01-26T14:33:47.5043414Z    | ^^^^^^^^
2026-01-26T14:33:47.5043601Z 95 |         for root, dirs, files in os.walk(root_dir):
2026-01-26T14:33:47.5043925Z 96 |             dirs[:] = [d for d in dirs if d not in ignored_dirs]
2026-01-26T14:33:47.5044192Z    |
2026-01-26T14:33:47.5044349Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5044507Z 
2026-01-26T14:33:47.5044594Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5044821Z   --> codebase_indexer.py:97:1
2026-01-26T14:33:47.5045017Z    |
2026-01-26T14:33:47.5045193Z 95 |         for root, dirs, files in os.walk(root_dir):
2026-01-26T14:33:47.5045501Z 96 |             dirs[:] = [d for d in dirs if d not in ignored_dirs]
2026-01-26T14:33:47.5045772Z 97 |             
2026-01-26T14:33:47.5045924Z    | ^^^^^^^^^^^^
2026-01-26T14:33:47.5046091Z 98 |             for file in files:
2026-01-26T14:33:47.5046647Z 99 |                 file_path = Path(root) / file
2026-01-26T14:33:47.5047061Z    |
2026-01-26T14:33:47.5047345Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5047613Z 
2026-01-26T14:33:47.5047731Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5047990Z    --> codebase_indexer.py:102:1
2026-01-26T14:33:47.5048197Z     |
2026-01-26T14:33:47.5048424Z 100 |                 if self.should_index_file(file_path, ignore_patterns):
2026-01-26T14:33:47.5049016Z 101 |                     indexable_files.append(file_path)
2026-01-26T14:33:47.5049345Z 102 |         
2026-01-26T14:33:47.5049505Z     | ^^^^^^^^
2026-01-26T14:33:47.5049680Z 103 |         return indexable_files
2026-01-26T14:33:47.5049890Z     |
2026-01-26T14:33:47.5050061Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5050231Z 
2026-01-26T14:33:47.5050314Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5050554Z    --> codebase_indexer.py:104:1
2026-01-26T14:33:47.5050753Z     |
2026-01-26T14:33:47.5050915Z 103 |         return indexable_files
2026-01-26T14:33:47.5051126Z 104 |     
2026-01-26T14:33:47.5051268Z     | ^^^^
2026-01-26T14:33:47.5051437Z 105 |     def process_file_to_chunks(
2026-01-26T14:33:47.5051655Z 106 |         self,
2026-01-26T14:33:47.5051817Z     |
2026-01-26T14:33:47.5051980Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5052144Z 
2026-01-26T14:33:47.5052228Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5052452Z    --> codebase_indexer.py:112:1
2026-01-26T14:33:47.5052649Z     |
2026-01-26T14:33:47.5052789Z 110 |         """
2026-01-26T14:33:47.5053062Z 111 |         Processes a single file: reads, splits into chunks, adds to indexer.
2026-01-26T14:33:47.5053410Z 112 |         
2026-01-26T14:33:47.5053561Z     | ^^^^^^^^
2026-01-26T14:33:47.5053872Z 113 |         Args:
2026-01-26T14:33:47.5054070Z 114 |             file_path: File to process
2026-01-26T14:33:47.5054311Z     |
2026-01-26T14:33:47.5054478Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5054649Z 
2026-01-26T14:33:47.5054840Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5055077Z    --> codebase_indexer.py:116:1
2026-01-26T14:33:47.5055286Z     |
2026-01-26T14:33:47.5055458Z 114 |             file_path: File to process
2026-01-26T14:33:47.5055753Z 115 |             indexer: Memory-limited indexer to add chunks to
2026-01-26T14:33:47.5056037Z 116 |             
2026-01-26T14:33:47.5056195Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5056358Z 117 |         Returns:
2026-01-26T14:33:47.5056579Z 118 |             True if file was successfully processed
2026-01-26T14:33:47.5056832Z     |
2026-01-26T14:33:47.5056995Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5057163Z 
2026-01-26T14:33:47.5057247Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5057496Z    --> codebase_indexer.py:124:1
2026-01-26T14:33:47.5057695Z     |
2026-01-26T14:33:47.5057863Z 122 |             if not content.strip():
2026-01-26T14:33:47.5058094Z 123 |                 return False
2026-01-26T14:33:47.5058298Z 124 |             
2026-01-26T14:33:47.5058452Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5058679Z 125 |             chunks = self.text_splitter.split_text(content)
2026-01-26T14:33:47.5059179Z     |
2026-01-26T14:33:47.5059376Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5059540Z 
2026-01-26T14:33:47.5059626Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5059858Z    --> codebase_indexer.py:126:1
2026-01-26T14:33:47.5060063Z     |
2026-01-26T14:33:47.5060265Z 125 |             chunks = self.text_splitter.split_text(content)
2026-01-26T14:33:47.5060545Z 126 |             
2026-01-26T14:33:47.5060705Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5060906Z 127 |             for i, chunk in enumerate(chunks):
2026-01-26T14:33:47.5061171Z 128 |                 indexer.add_chunk(
2026-01-26T14:33:47.5061391Z     |
2026-01-26T14:33:47.5061558Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5061718Z 
2026-01-26T14:33:47.5061800Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5062037Z    --> codebase_indexer.py:133:1
2026-01-26T14:33:47.5062231Z     |
2026-01-26T14:33:47.5062394Z 131 |                     f"{file_path}_{i}"
2026-01-26T14:33:47.5062617Z 132 |                 )
2026-01-26T14:33:47.5062794Z 133 |             
2026-01-26T14:33:47.5062944Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5063113Z 134 |             return True
2026-01-26T14:33:47.5063356Z 135 |         except (UnicodeDecodeError, IOError) as e:
2026-01-26T14:33:47.5063616Z     |
2026-01-26T14:33:47.5063784Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5063945Z 
2026-01-26T14:33:47.5064046Z UP024 [*] Replace aliased errors with `OSError`
2026-01-26T14:33:47.5064308Z    --> codebase_indexer.py:135:16
2026-01-26T14:33:47.5064514Z     |
2026-01-26T14:33:47.5064668Z 134 |             return True
2026-01-26T14:33:47.5064911Z 135 |         except (UnicodeDecodeError, IOError) as e:
2026-01-26T14:33:47.5065188Z     |                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5065519Z 136 |             logger.warning(f"Skipping {file_path}: encoding error - {e}")
2026-01-26T14:33:47.5065856Z 137 |             return False
2026-01-26T14:33:47.5066050Z     |
2026-01-26T14:33:47.5066214Z help: Replace with builtin `OSError`
2026-01-26T14:33:47.5066375Z 
2026-01-26T14:33:47.5066463Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5066704Z    --> codebase_indexer.py:141:1
2026-01-26T14:33:47.5066909Z     |
2026-01-26T14:33:47.5067197Z 139 |             logger.error(f"Unexpected error processing {file_path}: {e}", exc_info=True)
2026-01-26T14:33:47.5067571Z 140 |             return False
2026-01-26T14:33:47.5067767Z 141 |     
2026-01-26T14:33:47.5067948Z     | ^^^^
2026-01-26T14:33:47.5068125Z 142 |     def process_file_with_metadata(
2026-01-26T14:33:47.5068495Z 143 |         self,
2026-01-26T14:33:47.5068659Z     |
2026-01-26T14:33:47.5069052Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5069229Z 
2026-01-26T14:33:47.5069314Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5069661Z    --> codebase_indexer.py:150:1
2026-01-26T14:33:47.5069888Z     |
2026-01-26T14:33:47.5070027Z 148 |         """
2026-01-26T14:33:47.5070242Z 149 |         Processes a file and updates its metadata.
2026-01-26T14:33:47.5070500Z 150 |         
2026-01-26T14:33:47.5070654Z     | ^^^^^^^^
2026-01-26T14:33:47.5070818Z 151 |         Args:
2026-01-26T14:33:47.5071003Z 152 |             file_path: File to process
2026-01-26T14:33:47.5071231Z     |
2026-01-26T14:33:47.5071395Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5071560Z 
2026-01-26T14:33:47.5071642Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5071870Z    --> codebase_indexer.py:155:1
2026-01-26T14:33:47.5072077Z     |
2026-01-26T14:33:47.5072254Z 153 |             indexer: Memory-limited indexer
2026-01-26T14:33:47.5072534Z 154 |             metadata: Index metadata to update
2026-01-26T14:33:47.5072777Z 155 |             
2026-01-26T14:33:47.5072932Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5073099Z 156 |         Returns:
2026-01-26T14:33:47.5073316Z 157 |             True if file was successfully processed
2026-01-26T14:33:47.5073570Z     |
2026-01-26T14:33:47.5073735Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5073901Z 
2026-01-26T14:33:47.5073982Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5074234Z    --> codebase_indexer.py:161:1
2026-01-26T14:33:47.5074595Z     |
2026-01-26T14:33:47.5074825Z 159 |         if not self.process_file_to_chunks(file_path, indexer):
2026-01-26T14:33:47.5075125Z 160 |             return False
2026-01-26T14:33:47.5075319Z 161 |         
2026-01-26T14:33:47.5075470Z     | ^^^^^^^^
2026-01-26T14:33:47.5075621Z 162 |         try:
2026-01-26T14:33:47.5075808Z 163 |             mtime = file_path.stat().st_mtime
2026-01-26T14:33:47.5076049Z     |
2026-01-26T14:33:47.5076212Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5076377Z 
2026-01-26T14:33:47.5076461Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5076700Z    --> codebase_indexer.py:169:1
2026-01-26T14:33:47.5076897Z     |
2026-01-26T14:33:47.5077145Z 167 |             logger.error(f"Error updating metadata for {file_path}: {e}")
2026-01-26T14:33:47.5077467Z 168 |             return False
2026-01-26T14:33:47.5077662Z 169 |     
2026-01-26T14:33:47.5077805Z     | ^^^^
2026-01-26T14:33:47.5077962Z 170 |     def index_all(
2026-01-26T14:33:47.5078145Z 171 |         self,
2026-01-26T14:33:47.5078305Z     |
2026-01-26T14:33:47.5078471Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5078632Z 
2026-01-26T14:33:47.5078751Z UP006 [*] Use `set` instead of `Set` for type annotation
2026-01-26T14:33:47.5079156Z    --> codebase_indexer.py:173:23
2026-01-26T14:33:47.5079358Z     |
2026-01-26T14:33:47.5079499Z 171 |         self,
2026-01-26T14:33:47.5079675Z 172 |         root_dir: Path,
2026-01-26T14:33:47.5079882Z 173 |         ignored_dirs: Set[str],
2026-01-26T14:33:47.5080097Z     |                       ^^^
2026-01-26T14:33:47.5080312Z 174 |         ignore_patterns: Set[str],
2026-01-26T14:33:47.5080552Z 175 |         force: bool = False
2026-01-26T14:33:47.5080746Z     |
2026-01-26T14:33:47.5080901Z help: Replace with `set`
2026-01-26T14:33:47.5081024Z 
2026-01-26T14:33:47.5081139Z UP006 [*] Use `set` instead of `Set` for type annotation
2026-01-26T14:33:47.5081418Z    --> codebase_indexer.py:174:26
2026-01-26T14:33:47.5081617Z     |
2026-01-26T14:33:47.5081769Z 172 |         root_dir: Path,
2026-01-26T14:33:47.5081971Z 173 |         ignored_dirs: Set[str],
2026-01-26T14:33:47.5082204Z 174 |         ignore_patterns: Set[str],
2026-01-26T14:33:47.5082428Z     |                          ^^^
2026-01-26T14:33:47.5082640Z 175 |         force: bool = False
2026-01-26T14:33:47.5082842Z 176 |     ) -> str:
2026-01-26T14:33:47.5083125Z     |
2026-01-26T14:33:47.5083282Z help: Replace with `set`
2026-01-26T14:33:47.5083403Z 
2026-01-26T14:33:47.5083485Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5083715Z    --> codebase_indexer.py:179:1
2026-01-26T14:33:47.5083912Z     |
2026-01-26T14:33:47.5084155Z 177 |         """
2026-01-26T14:33:47.5084332Z 178 |         Indexes entire codebase.
2026-01-26T14:33:47.5084551Z 179 |         
2026-01-26T14:33:47.5084705Z     | ^^^^^^^^
2026-01-26T14:33:47.5084854Z 180 |         Args:
2026-01-26T14:33:47.5085047Z 181 |             root_dir: Root directory to index
2026-01-26T14:33:47.5085284Z     |
2026-01-26T14:33:47.5085453Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5085616Z 
2026-01-26T14:33:47.5085700Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5085928Z    --> codebase_indexer.py:185:1
2026-01-26T14:33:47.5086124Z     |
2026-01-26T14:33:47.5086321Z 183 |             ignore_patterns: File patterns to ignore
2026-01-26T14:33:47.5086627Z 184 |             force: If True, clears existing index first
2026-01-26T14:33:47.5086895Z 185 |             
2026-01-26T14:33:47.5087064Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5087223Z 186 |         Returns:
2026-01-26T14:33:47.5087441Z 187 |             Status message with indexing stats
2026-01-26T14:33:47.5087683Z     |
2026-01-26T14:33:47.5087859Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5087864Z 
2026-01-26T14:33:47.5087947Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5088029Z    --> codebase_indexer.py:194:1
2026-01-26T14:33:47.5088094Z     |
2026-01-26T14:33:47.5088163Z 192 |             if error:
2026-01-26T14:33:47.5088237Z 193 |                 return error
2026-01-26T14:33:47.5088304Z 194 |         
2026-01-26T14:33:47.5088365Z     | ^^^^^^^^
2026-01-26T14:33:47.5088485Z 195 |         def batch_upsert(documents, metadatas, ids):
2026-01-26T14:33:47.5088617Z 196 |             """Callback for flushing batches to vector store"""
2026-01-26T14:33:47.5088681Z     |
2026-01-26T14:33:47.5088872Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5088879Z 
2026-01-26T14:33:47.5088962Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5089053Z    --> codebase_indexer.py:204:1
2026-01-26T14:33:47.5089112Z     |
2026-01-26T14:33:47.5089198Z 202 |                     ids=ids[i:end]
2026-01-26T14:33:47.5089267Z 203 |                 )
2026-01-26T14:33:47.5089327Z 204 |         
2026-01-26T14:33:47.5089388Z     | ^^^^^^^^
2026-01-26T14:33:47.5089489Z 205 |         max_memory = get_max_memory_bytes()
2026-01-26T14:33:47.5089650Z 206 |         indexer = MemoryLimitedIndexer(max_memory, batch_upsert)
2026-01-26T14:33:47.5089710Z     |
2026-01-26T14:33:47.5089799Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5089804Z 
2026-01-26T14:33:47.5089893Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5089974Z    --> codebase_indexer.py:207:1
2026-01-26T14:33:47.5090033Z     |
2026-01-26T14:33:47.5090127Z 205 |         max_memory = get_max_memory_bytes()
2026-01-26T14:33:47.5090282Z 206 |         indexer = MemoryLimitedIndexer(max_memory, batch_upsert)
2026-01-26T14:33:47.5090343Z 207 |         
2026-01-26T14:33:47.5090403Z     | ^^^^^^^^
2026-01-26T14:33:47.5090639Z 208 |         logger.info(f"Scanning files (memory limit: {max_memory / 1024 / 1024:.0f} MB)...")
2026-01-26T14:33:47.5090699Z     |
2026-01-26T14:33:47.5090784Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5090789Z 
2026-01-26T14:33:47.5090875Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5090954Z    --> codebase_indexer.py:209:1
2026-01-26T14:33:47.5091012Z     |
2026-01-26T14:33:47.5091222Z 208 |         logger.info(f"Scanning files (memory limit: {max_memory / 1024 / 1024:.0f} MB)...")
2026-01-26T14:33:47.5091291Z 209 |         
2026-01-26T14:33:47.5091350Z     | ^^^^^^^^
2026-01-26T14:33:47.5091580Z 210 |         indexable_files = self.scan_indexable_files(root_dir, ignored_dirs, ignore_patterns)
2026-01-26T14:33:47.5091658Z 211 |         file_count = 0
2026-01-26T14:33:47.5091837Z     |
2026-01-26T14:33:47.5091928Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5091932Z 
2026-01-26T14:33:47.5092020Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5092102Z    --> codebase_indexer.py:212:1
2026-01-26T14:33:47.5092259Z     |
2026-01-26T14:33:47.5092499Z 210 |         indexable_files = self.scan_indexable_files(root_dir, ignored_dirs, ignore_patterns)
2026-01-26T14:33:47.5092575Z 211 |         file_count = 0
2026-01-26T14:33:47.5092636Z 212 |         
2026-01-26T14:33:47.5092697Z     | ^^^^^^^^
2026-01-26T14:33:47.5092802Z 213 |         for file_path in indexable_files:
2026-01-26T14:33:47.5092941Z 214 |             if self.process_file_to_chunks(file_path, indexer):
2026-01-26T14:33:47.5093001Z     |
2026-01-26T14:33:47.5093092Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5093097Z 
2026-01-26T14:33:47.5093178Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5093259Z    --> codebase_indexer.py:216:1
2026-01-26T14:33:47.5093321Z     |
2026-01-26T14:33:47.5093458Z 214 |             if self.process_file_to_chunks(file_path, indexer):
2026-01-26T14:33:47.5093533Z 215 |                 file_count += 1
2026-01-26T14:33:47.5093593Z 216 |         
2026-01-26T14:33:47.5093658Z     | ^^^^^^^^
2026-01-26T14:33:47.5093736Z 217 |         indexer.flush()
2026-01-26T14:33:47.5093797Z     |
2026-01-26T14:33:47.5093882Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5093892Z 
2026-01-26T14:33:47.5093972Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5094050Z    --> codebase_indexer.py:218:1
2026-01-26T14:33:47.5094108Z     |
2026-01-26T14:33:47.5094187Z 217 |         indexer.flush()
2026-01-26T14:33:47.5094248Z 218 |         
2026-01-26T14:33:47.5094308Z     | ^^^^^^^^
2026-01-26T14:33:47.5094399Z 219 |         stats = indexer.get_stats()
2026-01-26T14:33:47.5094694Z 220 |         return f"Indexed {file_count} files ({stats['total_chunks']} chunks in {stats['total_batches']} batches)."
2026-01-26T14:33:47.5094754Z     |
2026-01-26T14:33:47.5094843Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5094848Z 
2026-01-26T14:33:47.5094935Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5095015Z    --> codebase_indexer.py:221:1
2026-01-26T14:33:47.5095074Z     |
2026-01-26T14:33:47.5095167Z 219 |         stats = indexer.get_stats()
2026-01-26T14:33:47.5095446Z 220 |         return f"Indexed {file_count} files ({stats['total_chunks']} chunks in {stats['total_batches']} batches)."
2026-01-26T14:33:47.5095508Z 221 |     
2026-01-26T14:33:47.5095573Z     | ^^^^
2026-01-26T14:33:47.5095646Z 222 |     def index_changed(
2026-01-26T14:33:47.5095708Z 223 |         self,
2026-01-26T14:33:47.5095767Z     |
2026-01-26T14:33:47.5095858Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5095862Z 
2026-01-26T14:33:47.5095986Z UP006 [*] Use `set` instead of `Set` for type annotation
2026-01-26T14:33:47.5096071Z    --> codebase_indexer.py:225:23
2026-01-26T14:33:47.5096135Z     |
2026-01-26T14:33:47.5096201Z 223 |         self,
2026-01-26T14:33:47.5096273Z 224 |         root_dir: Path,
2026-01-26T14:33:47.5096351Z 225 |         ignored_dirs: Set[str],
2026-01-26T14:33:47.5096425Z     |                       ^^^
2026-01-26T14:33:47.5096507Z 226 |         ignore_patterns: Set[str]
2026-01-26T14:33:47.5096573Z 227 |     ) -> str:
2026-01-26T14:33:47.5096634Z     |
2026-01-26T14:33:47.5096709Z help: Replace with `set`
2026-01-26T14:33:47.5096714Z 
2026-01-26T14:33:47.5096829Z UP006 [*] Use `set` instead of `Set` for type annotation
2026-01-26T14:33:47.5096911Z    --> codebase_indexer.py:226:26
2026-01-26T14:33:47.5096969Z     |
2026-01-26T14:33:47.5097041Z 224 |         root_dir: Path,
2026-01-26T14:33:47.5097116Z 225 |         ignored_dirs: Set[str],
2026-01-26T14:33:47.5097200Z 226 |         ignore_patterns: Set[str]
2026-01-26T14:33:47.5097270Z     |                          ^^^
2026-01-26T14:33:47.5097333Z 227 |     ) -> str:
2026-01-26T14:33:47.5097398Z 228 |         """
2026-01-26T14:33:47.5097455Z     |
2026-01-26T14:33:47.5097619Z help: Replace with `set`
2026-01-26T14:33:47.5097624Z 
2026-01-26T14:33:47.5097706Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5097790Z    --> codebase_indexer.py:230:1
2026-01-26T14:33:47.5097847Z     |
2026-01-26T14:33:47.5098027Z 228 |         """
2026-01-26T14:33:47.5098169Z 229 |         Indexes only changed files (incremental indexing).
2026-01-26T14:33:47.5098230Z 230 |         
2026-01-26T14:33:47.5098291Z     | ^^^^^^^^
2026-01-26T14:33:47.5098353Z 231 |         Args:
2026-01-26T14:33:47.5098454Z 232 |             root_dir: Root directory to scan
2026-01-26T14:33:47.5098514Z     |
2026-01-26T14:33:47.5098600Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5098604Z 
2026-01-26T14:33:47.5098690Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5098870Z    --> codebase_indexer.py:235:1
2026-01-26T14:33:47.5098931Z     |
2026-01-26T14:33:47.5099038Z 233 |             ignored_dirs: Directories to skip
2026-01-26T14:33:47.5099152Z 234 |             ignore_patterns: File patterns to ignore
2026-01-26T14:33:47.5099217Z 235 |             
2026-01-26T14:33:47.5099279Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5099350Z 236 |         Returns:
2026-01-26T14:33:47.5099449Z 237 |             Status message with indexing stats
2026-01-26T14:33:47.5099513Z     |
2026-01-26T14:33:47.5099603Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5099607Z 
2026-01-26T14:33:47.5099688Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5099767Z    --> codebase_indexer.py:240:1
2026-01-26T14:33:47.5099830Z     |
2026-01-26T14:33:47.5099891Z 238 |         """
2026-01-26T14:33:47.5099979Z 239 |         metadata = IndexMetadata()
2026-01-26T14:33:47.5100040Z 240 |         
2026-01-26T14:33:47.5100105Z     | ^^^^^^^^
2026-01-26T14:33:47.5100317Z 241 |         all_files = self.scan_indexable_files(root_dir, ignored_dirs, ignore_patterns)
2026-01-26T14:33:47.5100456Z 242 |         changed_files = metadata.get_changed_files(all_files)
2026-01-26T14:33:47.5100521Z     |
2026-01-26T14:33:47.5100612Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5100617Z 
2026-01-26T14:33:47.5100700Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5100778Z    --> codebase_indexer.py:243:1
2026-01-26T14:33:47.5100844Z     |
2026-01-26T14:33:47.5101047Z 241 |         all_files = self.scan_indexable_files(root_dir, ignored_dirs, ignore_patterns)
2026-01-26T14:33:47.5101180Z 242 |         changed_files = metadata.get_changed_files(all_files)
2026-01-26T14:33:47.5101248Z 243 |         
2026-01-26T14:33:47.5101308Z     | ^^^^^^^^
2026-01-26T14:33:47.5101385Z 244 |         if not changed_files:
2026-01-26T14:33:47.5101491Z 245 |             return "No changed files to index."
2026-01-26T14:33:47.5101550Z     |
2026-01-26T14:33:47.5101636Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5101640Z 
2026-01-26T14:33:47.5101720Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5101805Z    --> codebase_indexer.py:246:1
2026-01-26T14:33:47.5101867Z     |
2026-01-26T14:33:47.5101944Z 244 |         if not changed_files:
2026-01-26T14:33:47.5102047Z 245 |             return "No changed files to index."
2026-01-26T14:33:47.5102107Z 246 |         
2026-01-26T14:33:47.5102166Z     | ^^^^^^^^
2026-01-26T14:33:47.5102293Z 247 |         def batch_upsert(documents, metadatas, ids):
2026-01-26T14:33:47.5102423Z 248 |             """Callback for flushing batches to vector store"""
2026-01-26T14:33:47.5102482Z     |
2026-01-26T14:33:47.5102567Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5102572Z 
2026-01-26T14:33:47.5102654Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5102732Z    --> codebase_indexer.py:256:1
2026-01-26T14:33:47.5102789Z     |
2026-01-26T14:33:47.5102871Z 254 |                     ids=ids[i:end]
2026-01-26T14:33:47.5102936Z 255 |                 )
2026-01-26T14:33:47.5102995Z 256 |         
2026-01-26T14:33:47.5103055Z     | ^^^^^^^^
2026-01-26T14:33:47.5103155Z 257 |         max_memory = get_max_memory_bytes()
2026-01-26T14:33:47.5103425Z 258 |         indexer = MemoryLimitedIndexer(max_memory, batch_upsert)
2026-01-26T14:33:47.5103484Z     |
2026-01-26T14:33:47.5103574Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5103579Z 
2026-01-26T14:33:47.5103762Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5103844Z    --> codebase_indexer.py:259:1
2026-01-26T14:33:47.5103908Z     |
2026-01-26T14:33:47.5103999Z 257 |         max_memory = get_max_memory_bytes()
2026-01-26T14:33:47.5104142Z 258 |         indexer = MemoryLimitedIndexer(max_memory, batch_upsert)
2026-01-26T14:33:47.5104202Z 259 |         
2026-01-26T14:33:47.5104268Z     | ^^^^^^^^
2026-01-26T14:33:47.5104564Z 260 |         logger.info(f"Found {len(changed_files)} changed files (memory limit: {max_memory / 1024 / 1024:.0f} MB)...")
2026-01-26T14:33:47.5104636Z 261 |         file_count = 0
2026-01-26T14:33:47.5104700Z     |
2026-01-26T14:33:47.5104784Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5104788Z 
2026-01-26T14:33:47.5104876Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5104959Z    --> codebase_indexer.py:262:1
2026-01-26T14:33:47.5105019Z     |
2026-01-26T14:33:47.5105309Z 260 |         logger.info(f"Found {len(changed_files)} changed files (memory limit: {max_memory / 1024 / 1024:.0f} MB)...")
2026-01-26T14:33:47.5105379Z 261 |         file_count = 0
2026-01-26T14:33:47.5105446Z 262 |         
2026-01-26T14:33:47.5105506Z     | ^^^^^^^^
2026-01-26T14:33:47.5105600Z 263 |         for file_path in changed_files:
2026-01-26T14:33:47.5105783Z 264 |             if self.process_file_with_metadata(file_path, indexer, metadata):
2026-01-26T14:33:47.5105844Z     |
2026-01-26T14:33:47.5105928Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5105933Z 
2026-01-26T14:33:47.5106019Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5106097Z    --> codebase_indexer.py:266:1
2026-01-26T14:33:47.5106155Z     |
2026-01-26T14:33:47.5106324Z 264 |             if self.process_file_with_metadata(file_path, indexer, metadata):
2026-01-26T14:33:47.5106410Z 265 |                 file_count += 1
2026-01-26T14:33:47.5106470Z 266 |         
2026-01-26T14:33:47.5106530Z     | ^^^^^^^^
2026-01-26T14:33:47.5106609Z 267 |         indexer.flush()
2026-01-26T14:33:47.5106667Z     |
2026-01-26T14:33:47.5106754Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5106758Z 
2026-01-26T14:33:47.5106843Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5106919Z    --> codebase_indexer.py:268:1
2026-01-26T14:33:47.5106977Z     |
2026-01-26T14:33:47.5107048Z 267 |         indexer.flush()
2026-01-26T14:33:47.5107114Z 268 |         
2026-01-26T14:33:47.5107174Z     | ^^^^^^^^
2026-01-26T14:33:47.5107289Z 269 |         existing_files = {str(f) for f in all_files}
2026-01-26T14:33:47.5107415Z 270 |         metadata.remove_deleted_files(existing_files)
2026-01-26T14:33:47.5107474Z     |
2026-01-26T14:33:47.5107559Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5107563Z 
2026-01-26T14:33:47.5107647Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5107735Z    --> codebase_indexer.py:272:1
2026-01-26T14:33:47.5107792Z     |
2026-01-26T14:33:47.5108172Z 270 | …     metadata.remove_deleted_files(existing_files)
2026-01-26T14:33:47.5108297Z 271 | …     metadata.save()
2026-01-26T14:33:47.5108382Z 272 | …     
2026-01-26T14:33:47.5108444Z     ^^^^^^^^
2026-01-26T14:33:47.5108564Z 273 | …     stats = indexer.get_stats()
2026-01-26T14:33:47.5109151Z 274 | …     return f"Incrementally indexed {file_count} changed files ({stats['total_chunks']} chunks in {stats['total_batches']} batches)."
2026-01-26T14:33:47.5109214Z     |
2026-01-26T14:33:47.5109302Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5109308Z 
2026-01-26T14:33:47.5109444Z UP035 `typing.Set` is deprecated, use `set` instead
2026-01-26T14:33:47.5109533Z  --> config.py:3:1
2026-01-26T14:33:47.5109594Z   |
2026-01-26T14:33:47.5109662Z 1 | import os
2026-01-26T14:33:47.5109742Z 2 | from pathlib import Path
2026-01-26T14:33:47.5109953Z 3 | from typing import Set
2026-01-26T14:33:47.5110021Z   | ^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5110085Z 4 |
2026-01-26T14:33:47.5110171Z 5 | PROJECT_ROOT = Path.cwd().resolve()
2026-01-26T14:33:47.5110229Z   |
2026-01-26T14:33:47.5110235Z 
2026-01-26T14:33:47.5110467Z UP006 [*] Use `set` instead of `Set` for type annotation
2026-01-26T14:33:47.5110545Z   --> config.py:27:23
2026-01-26T14:33:47.5110605Z    |
2026-01-26T14:33:47.5110677Z 25 | MAX_MEMORY_MB = 100
2026-01-26T14:33:47.5110743Z 26 |
2026-01-26T14:33:47.5110827Z 27 | DEFAULT_IGNORED_DIRS: Set[str] = {
2026-01-26T14:33:47.5110897Z    |                       ^^^
2026-01-26T14:33:47.5110965Z 28 |     ".git",
2026-01-26T14:33:47.5111034Z 29 |     "node_modules",
2026-01-26T14:33:47.5111093Z    |
2026-01-26T14:33:47.5111170Z help: Replace with `set`
2026-01-26T14:33:47.5111179Z 
2026-01-26T14:33:47.5111296Z UP006 [*] Use `set` instead of `Set` for type annotation
2026-01-26T14:33:47.5111366Z   --> config.py:47:20
2026-01-26T14:33:47.5111423Z    |
2026-01-26T14:33:47.5111494Z 45 | }
2026-01-26T14:33:47.5111552Z 46 |
2026-01-26T14:33:47.5111636Z 47 | BINARY_EXTENSIONS: Set[str] = {
2026-01-26T14:33:47.5111708Z    |                    ^^^
2026-01-26T14:33:47.5111772Z 48 |     ".pyc",
2026-01-26T14:33:47.5111838Z 49 |     ".pyo",
2026-01-26T14:33:47.5111896Z    |
2026-01-26T14:33:47.5111975Z help: Replace with `set`
2026-01-26T14:33:47.5111979Z 
2026-01-26T14:33:47.5112093Z UP006 [*] Use `set` instead of `Set` for type annotation
2026-01-26T14:33:47.5112162Z   --> config.py:81:18
2026-01-26T14:33:47.5112227Z    |
2026-01-26T14:33:47.5112287Z 79 | }
2026-01-26T14:33:47.5112344Z 80 |
2026-01-26T14:33:47.5112425Z 81 | CODE_EXTENSIONS: Set[str] = {
2026-01-26T14:33:47.5112497Z    |                  ^^^
2026-01-26T14:33:47.5112561Z 82 |     ".py",
2026-01-26T14:33:47.5112622Z 83 |     ".js",
2026-01-26T14:33:47.5112686Z    |
2026-01-26T14:33:47.5112758Z help: Replace with `set`
2026-01-26T14:33:47.5112762Z 
2026-01-26T14:33:47.5112876Z UP006 [*] Use `set` instead of `Set` for type annotation
2026-01-26T14:33:47.5112953Z    --> config.py:109:18
2026-01-26T14:33:47.5113017Z     |
2026-01-26T14:33:47.5113077Z 107 | }
2026-01-26T14:33:47.5113136Z 108 |
2026-01-26T14:33:47.5113222Z 109 | TEXT_EXTENSIONS: Set[str] = {
2026-01-26T14:33:47.5113292Z     |                  ^^^
2026-01-26T14:33:47.5113354Z 110 |     ".txt",
2026-01-26T14:33:47.5113416Z 111 |     ".md",
2026-01-26T14:33:47.5113482Z     |
2026-01-26T14:33:47.5113555Z help: Replace with `set`
2026-01-26T14:33:47.5113559Z 
2026-01-26T14:33:47.5113670Z UP006 [*] Use `set` instead of `Set` for type annotation
2026-01-26T14:33:47.5113749Z    --> config.py:154:27
2026-01-26T14:33:47.5113809Z     |
2026-01-26T14:33:47.5113900Z 154 | def get_ignored_dirs() -> Set[str]:
2026-01-26T14:33:47.5113973Z     |                           ^^^
2026-01-26T14:33:47.5114069Z 155 |     return DEFAULT_IGNORED_DIRS.copy()
2026-01-26T14:33:47.5114127Z     |
2026-01-26T14:33:47.5114208Z help: Replace with `set`
2026-01-26T14:33:47.5114217Z 
2026-01-26T14:33:47.5114305Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5114378Z    --> config.py:162:1
2026-01-26T14:33:47.5114440Z     |
2026-01-26T14:33:47.5114608Z 160 |     Validates that a path is within the project root directory.
2026-01-26T14:33:47.5114703Z 161 |     Prevents path traversal attacks.
2026-01-26T14:33:47.5114766Z 162 |     
2026-01-26T14:33:47.5114826Z     | ^^^^
2026-01-26T14:33:47.5114894Z 163 |     Args:
2026-01-26T14:33:47.5114985Z 164 |         path: Path string to validate
2026-01-26T14:33:47.5115045Z     |
2026-01-26T14:33:47.5115137Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5115142Z 
2026-01-26T14:33:47.5115225Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5115297Z    --> config.py:165:1
2026-01-26T14:33:47.5115361Z     |
2026-01-26T14:33:47.5115422Z 163 |     Args:
2026-01-26T14:33:47.5115506Z 164 |         path: Path string to validate
2026-01-26T14:33:47.5115567Z 165 |         
2026-01-26T14:33:47.5115633Z     | ^^^^^^^^
2026-01-26T14:33:47.5115784Z 166 |     Returns:
2026-01-26T14:33:47.5115865Z 167 |         Resolved Path object
2026-01-26T14:33:47.5115930Z     |
2026-01-26T14:33:47.5116016Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5116021Z 
2026-01-26T14:33:47.5116170Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5116243Z    --> config.py:168:1
2026-01-26T14:33:47.5116310Z     |
2026-01-26T14:33:47.5116372Z 166 |     Returns:
2026-01-26T14:33:47.5116448Z 167 |         Resolved Path object
2026-01-26T14:33:47.5116514Z 168 |         
2026-01-26T14:33:47.5116573Z     | ^^^^^^^^
2026-01-26T14:33:47.5116637Z 169 |     Raises:
2026-01-26T14:33:47.5116780Z 170 |         ValueError: If path is outside project root or invalid
2026-01-26T14:33:47.5116844Z     |
2026-01-26T14:33:47.5116930Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5116935Z 
2026-01-26T14:33:47.5117015Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5117092Z    --> config.py:175:1
2026-01-26T14:33:47.5117154Z     |
2026-01-26T14:33:47.5117267Z 173 |         if not path or not isinstance(path, str):
2026-01-26T14:33:47.5117408Z 174 |             raise ValueError("Path must be a non-empty string")
2026-01-26T14:33:47.5117469Z 175 |         
2026-01-26T14:33:47.5117532Z     | ^^^^^^^^
2026-01-26T14:33:47.5117629Z 176 |         target_path = Path(path).resolve()
2026-01-26T14:33:47.5117693Z     |
2026-01-26T14:33:47.5117777Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5117781Z 
2026-01-26T14:33:47.5117862Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5117937Z    --> config.py:177:1
2026-01-26T14:33:47.5117997Z     |
2026-01-26T14:33:47.5118090Z 176 |         target_path = Path(path).resolve()
2026-01-26T14:33:47.5118152Z 177 |         
2026-01-26T14:33:47.5118217Z     | ^^^^^^^^
2026-01-26T14:33:47.5118346Z 178 |         if not target_path.is_relative_to(PROJECT_ROOT):
2026-01-26T14:33:47.5118420Z 179 |             raise ValueError(
2026-01-26T14:33:47.5118485Z     |
2026-01-26T14:33:47.5118573Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5118578Z 
2026-01-26T14:33:47.5118659Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5118734Z    --> config.py:183:1
2026-01-26T14:33:47.5118895Z     |
2026-01-26T14:33:47.5119033Z 181 |                 f"Only paths within {PROJECT_ROOT} are allowed."
2026-01-26T14:33:47.5119096Z 182 |             )
2026-01-26T14:33:47.5119162Z 183 |         
2026-01-26T14:33:47.5119225Z     | ^^^^^^^^
2026-01-26T14:33:47.5119303Z 184 |         return target_path
2026-01-26T14:33:47.5119407Z 185 |     except (OSError, RuntimeError) as e:
2026-01-26T14:33:47.5119467Z     |
2026-01-26T14:33:47.5119551Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5119555Z 
2026-01-26T14:33:47.5119981Z B904 Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
2026-01-26T14:33:47.5120059Z    --> config.py:186:9
2026-01-26T14:33:47.5120117Z     |
2026-01-26T14:33:47.5120198Z 184 |         return target_path
2026-01-26T14:33:47.5120302Z 185 |     except (OSError, RuntimeError) as e:
2026-01-26T14:33:47.5120429Z 186 |         raise ValueError(f"Invalid path '{path}': {e}")
2026-01-26T14:33:47.5120522Z     |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5120587Z     |
2026-01-26T14:33:47.5120592Z 
2026-01-26T14:33:47.5120673Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5120744Z    --> config.py:194:1
2026-01-26T14:33:47.5120807Z     |
2026-01-26T14:33:47.5120941Z 192 |     Tries multiple encodings instead of ignoring errors.
2026-01-26T14:33:47.5121046Z 193 |     Uses FileCache for improved performance.
2026-01-26T14:33:47.5121106Z 194 |     
2026-01-26T14:33:47.5121171Z     | ^^^^
2026-01-26T14:33:47.5121233Z 195 |     Args:
2026-01-26T14:33:47.5121330Z 196 |         file_path: Path to the file to read
2026-01-26T14:33:47.5121393Z     |
2026-01-26T14:33:47.5121479Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5121604Z 
2026-01-26T14:33:47.5121689Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5121764Z    --> config.py:197:1
2026-01-26T14:33:47.5121829Z     |
2026-01-26T14:33:47.5121891Z 195 |     Args:
2026-01-26T14:33:47.5122091Z 196 |         file_path: Path to the file to read
2026-01-26T14:33:47.5122160Z 197 |         
2026-01-26T14:33:47.5122220Z     | ^^^^^^^^
2026-01-26T14:33:47.5122285Z 198 |     Returns:
2026-01-26T14:33:47.5122364Z 199 |         File content as string
2026-01-26T14:33:47.5122428Z     |
2026-01-26T14:33:47.5122513Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5122518Z 
2026-01-26T14:33:47.5122597Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5122672Z    --> config.py:200:1
2026-01-26T14:33:47.5122730Z     |
2026-01-26T14:33:47.5122792Z 198 |     Returns:
2026-01-26T14:33:47.5122880Z 199 |         File content as string
2026-01-26T14:33:47.5122940Z 200 |         
2026-01-26T14:33:47.5123001Z     | ^^^^^^^^
2026-01-26T14:33:47.5123063Z 201 |     Raises:
2026-01-26T14:33:47.5123282Z 202 |         UnicodeDecodeError: If file cannot be decoded with any supported encoding
2026-01-26T14:33:47.5123342Z     |
2026-01-26T14:33:47.5123428Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5123432Z 
2026-01-26T14:33:47.5123523Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5123596Z    --> config.py:209:1
2026-01-26T14:33:47.5123655Z     |
2026-01-26T14:33:47.5123750Z 207 |         from cache_manager import FileCache
2026-01-26T14:33:47.5123851Z 208 |         _file_cache = FileCache(capacity=50)
2026-01-26T14:33:47.5123911Z 209 |     
2026-01-26T14:33:47.5123971Z     | ^^^^
2026-01-26T14:33:47.5124085Z 210 |     cached_content = _file_cache.get(file_path)
2026-01-26T14:33:47.5124171Z 211 |     if cached_content is not None:
2026-01-26T14:33:47.5124229Z     |
2026-01-26T14:33:47.5124319Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5124323Z 
2026-01-26T14:33:47.5124404Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5124478Z    --> config.py:213:1
2026-01-26T14:33:47.5124539Z     |
2026-01-26T14:33:47.5124628Z 211 |     if cached_content is not None:
2026-01-26T14:33:47.5124702Z 212 |         return cached_content
2026-01-26T14:33:47.5124762Z 213 |     
2026-01-26T14:33:47.5124830Z     | ^^^^
2026-01-26T14:33:47.5124998Z 214 |     encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252', 'iso-8859-1']
2026-01-26T14:33:47.5125057Z     |
2026-01-26T14:33:47.5125143Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5125152Z 
2026-01-26T14:33:47.5125233Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5125303Z    --> config.py:215:1
2026-01-26T14:33:47.5125362Z     |
2026-01-26T14:33:47.5125529Z 214 |     encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252', 'iso-8859-1']
2026-01-26T14:33:47.5125597Z 215 |     
2026-01-26T14:33:47.5125668Z     | ^^^^
2026-01-26T14:33:47.5125750Z 216 |     for encoding in encodings:
2026-01-26T14:33:47.5125813Z 217 |         try:
2026-01-26T14:33:47.5125872Z     |
2026-01-26T14:33:47.5125960Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5125965Z 
2026-01-26T14:33:47.5126384Z B904 Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
2026-01-26T14:33:47.5126457Z    --> config.py:224:13
2026-01-26T14:33:47.5126515Z     |
2026-01-26T14:33:47.5126590Z 222 |             continue
2026-01-26T14:33:47.5126668Z 223 |         except Exception as e:
2026-01-26T14:33:47.5126809Z 224 |             raise IOError(f"Error reading file {file_path}: {e}")
2026-01-26T14:33:47.5126911Z     |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5126971Z 225 |     
2026-01-26T14:33:47.5127053Z 226 |     raise UnicodeDecodeError(
2026-01-26T14:33:47.5127114Z     |
2026-01-26T14:33:47.5127119Z 
2026-01-26T14:33:47.5127226Z UP024 [*] Replace aliased errors with `OSError`
2026-01-26T14:33:47.5127298Z    --> config.py:224:19
2026-01-26T14:33:47.5127357Z     |
2026-01-26T14:33:47.5127525Z 222 |             continue
2026-01-26T14:33:47.5127603Z 223 |         except Exception as e:
2026-01-26T14:33:47.5127741Z 224 |             raise IOError(f"Error reading file {file_path}: {e}")
2026-01-26T14:33:47.5127891Z     |                   ^^^^^^^
2026-01-26T14:33:47.5127956Z 225 |     
2026-01-26T14:33:47.5128044Z 226 |     raise UnicodeDecodeError(
2026-01-26T14:33:47.5128103Z     |
2026-01-26T14:33:47.5128221Z help: Replace `IOError` with builtin `OSError`
2026-01-26T14:33:47.5128226Z 
2026-01-26T14:33:47.5128311Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5128385Z    --> config.py:225:1
2026-01-26T14:33:47.5128450Z     |
2026-01-26T14:33:47.5128527Z 223 |         except Exception as e:
2026-01-26T14:33:47.5128668Z 224 |             raise IOError(f"Error reading file {file_path}: {e}")
2026-01-26T14:33:47.5128728Z 225 |     
2026-01-26T14:33:47.5128895Z     | ^^^^
2026-01-26T14:33:47.5128980Z 226 |     raise UnicodeDecodeError(
2026-01-26T14:33:47.5129060Z 227 |         'multi-encoding',
2026-01-26T14:33:47.5129125Z     |
2026-01-26T14:33:47.5129212Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5129218Z 
2026-01-26T14:33:47.5129300Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5129380Z    --> config.py:238:1
2026-01-26T14:33:47.5129439Z     |
2026-01-26T14:33:47.5129500Z 236 |     """
2026-01-26T14:33:47.5129586Z 237 |     Returns file cache statistics.
2026-01-26T14:33:47.5129650Z 238 |     
2026-01-26T14:33:47.5129710Z     | ^^^^
2026-01-26T14:33:47.5129773Z 239 |     Returns:
2026-01-26T14:33:47.5129870Z 240 |         Dictionary with cache statistics
2026-01-26T14:33:47.5129929Z     |
2026-01-26T14:33:47.5130015Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5130021Z 
2026-01-26T14:33:47.5130126Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5130222Z   --> incremental_indexing.py:1:1
2026-01-26T14:33:47.5130282Z    |
2026-01-26T14:33:47.5130347Z  1 | / import json
2026-01-26T14:33:47.5130417Z  2 | | import os
2026-01-26T14:33:47.5130481Z  3 | | import sys
2026-01-26T14:33:47.5130551Z  4 | | import tempfile
2026-01-26T14:33:47.5130630Z  5 | | from pathlib import Path
2026-01-26T14:33:47.5130722Z  6 | | from typing import Dict, List, Set
2026-01-26T14:33:47.5130803Z  7 | | from datetime import datetime
2026-01-26T14:33:47.5130897Z  8 | | from contextlib import contextmanager
2026-01-26T14:33:47.5130962Z  9 | |
2026-01-26T14:33:47.5131054Z 10 | | from config import INDEX_METADATA_FILE
2026-01-26T14:33:47.5131133Z    | |______________________________________^
2026-01-26T14:33:47.5131192Z 11 |
2026-01-26T14:33:47.5131276Z 12 |   if sys.platform == 'win32':
2026-01-26T14:33:47.5131333Z    |
2026-01-26T14:33:47.5131407Z help: Organize imports
2026-01-26T14:33:47.5131412Z 
2026-01-26T14:33:47.5131538Z UP035 `typing.Dict` is deprecated, use `dict` instead
2026-01-26T14:33:47.5131623Z  --> incremental_indexing.py:6:1
2026-01-26T14:33:47.5131682Z   |
2026-01-26T14:33:47.5131757Z 4 | import tempfile
2026-01-26T14:33:47.5131839Z 5 | from pathlib import Path
2026-01-26T14:33:47.5131926Z 6 | from typing import Dict, List, Set
2026-01-26T14:33:47.5131996Z   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5132081Z 7 | from datetime import datetime
2026-01-26T14:33:47.5132173Z 8 | from contextlib import contextmanager
2026-01-26T14:33:47.5132232Z   |
2026-01-26T14:33:47.5132236Z 
2026-01-26T14:33:47.5132357Z UP035 `typing.List` is deprecated, use `list` instead
2026-01-26T14:33:47.5132438Z  --> incremental_indexing.py:6:1
2026-01-26T14:33:47.5132497Z   |
2026-01-26T14:33:47.5132563Z 4 | import tempfile
2026-01-26T14:33:47.5132646Z 5 | from pathlib import Path
2026-01-26T14:33:47.5132729Z 6 | from typing import Dict, List, Set
2026-01-26T14:33:47.5132796Z   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5132880Z 7 | from datetime import datetime
2026-01-26T14:33:47.5132966Z 8 | from contextlib import contextmanager
2026-01-26T14:33:47.5133024Z   |
2026-01-26T14:33:47.5133029Z 
2026-01-26T14:33:47.5133268Z UP035 `typing.Set` is deprecated, use `set` instead
2026-01-26T14:33:47.5133351Z  --> incremental_indexing.py:6:1
2026-01-26T14:33:47.5133410Z   |
2026-01-26T14:33:47.5133477Z 4 | import tempfile
2026-01-26T14:33:47.5133558Z 5 | from pathlib import Path
2026-01-26T14:33:47.5133737Z 6 | from typing import Dict, List, Set
2026-01-26T14:33:47.5133809Z   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5133893Z 7 | from datetime import datetime
2026-01-26T14:33:47.5133980Z 8 | from contextlib import contextmanager
2026-01-26T14:33:47.5134038Z   |
2026-01-26T14:33:47.5134043Z 
2026-01-26T14:33:47.5134123Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5134212Z   --> incremental_indexing.py:47:1
2026-01-26T14:33:47.5134271Z    |
2026-01-26T14:33:47.5134428Z 45 |     Atomically writes content to a file using temp file + rename.
2026-01-26T14:33:47.5134536Z 46 |     Prevents partial writes and corruption.
2026-01-26T14:33:47.5134596Z 47 |     
2026-01-26T14:33:47.5134655Z    | ^^^^
2026-01-26T14:33:47.5134724Z 48 |     Args:
2026-01-26T14:33:47.5134816Z 49 |         file_path: Target file path
2026-01-26T14:33:47.5134874Z    |
2026-01-26T14:33:47.5134960Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5134965Z 
2026-01-26T14:33:47.5135052Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5135136Z   --> incremental_indexing.py:51:1
2026-01-26T14:33:47.5135195Z    |
2026-01-26T14:33:47.5135281Z 49 |         file_path: Target file path
2026-01-26T14:33:47.5135359Z 50 |         content: Content to write
2026-01-26T14:33:47.5135419Z 51 |         
2026-01-26T14:33:47.5135479Z    | ^^^^^^^^
2026-01-26T14:33:47.5135550Z 52 |     Raises:
2026-01-26T14:33:47.5135645Z 53 |         IOError: If write operation fails
2026-01-26T14:33:47.5135703Z    |
2026-01-26T14:33:47.5135800Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5135805Z 
2026-01-26T14:33:47.5135886Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5135968Z   --> incremental_indexing.py:56:1
2026-01-26T14:33:47.5136035Z    |
2026-01-26T14:33:47.5136099Z 54 |     """
2026-01-26T14:33:47.5136230Z 55 |     file_path.parent.mkdir(parents=True, exist_ok=True)
2026-01-26T14:33:47.5136290Z 56 |     
2026-01-26T14:33:47.5136378Z    | ^^^^
2026-01-26T14:33:47.5136473Z 57 |     fd, temp_path = tempfile.mkstemp(
2026-01-26T14:33:47.5136550Z 58 |         dir=file_path.parent,
2026-01-26T14:33:47.5136629Z    |
2026-01-26T14:33:47.5136728Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5136732Z 
2026-01-26T14:33:47.5136814Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5136895Z   --> incremental_indexing.py:62:1
2026-01-26T14:33:47.5136960Z    |
2026-01-26T14:33:47.5137032Z 60 |         suffix=".tmp"
2026-01-26T14:33:47.5137093Z 61 |     )
2026-01-26T14:33:47.5137156Z 62 |     
2026-01-26T14:33:47.5137216Z    | ^^^^
2026-01-26T14:33:47.5137278Z 63 |     try:
2026-01-26T14:33:47.5137394Z 64 |         with os.fdopen(fd, 'w', encoding='utf-8') as f:
2026-01-26T14:33:47.5137458Z    |
2026-01-26T14:33:47.5137547Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5137552Z 
2026-01-26T14:33:47.5137632Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5137718Z   --> incremental_indexing.py:68:1
2026-01-26T14:33:47.5137777Z    |
2026-01-26T14:33:47.5137847Z 66 |             f.flush()
2026-01-26T14:33:47.5137934Z 67 |             os.fsync(f.fileno())
2026-01-26T14:33:47.5137993Z 68 |         
2026-01-26T14:33:47.5138053Z    | ^^^^^^^^
2026-01-26T14:33:47.5138134Z 69 |         if sys.platform == 'win32':
2026-01-26T14:33:47.5138206Z 70 |             try:
2026-01-26T14:33:47.5138281Z    |
2026-01-26T14:33:47.5138365Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5138369Z 
2026-01-26T14:33:47.5138454Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5138534Z   --> incremental_indexing.py:75:1
2026-01-26T14:33:47.5138592Z    |
2026-01-26T14:33:47.5138680Z 73 |             except FileNotFoundError:
2026-01-26T14:33:47.5138756Z 74 |                 pass
2026-01-26T14:33:47.5139059Z 75 |         
2026-01-26T14:33:47.5139119Z    | ^^^^^^^^
2026-01-26T14:33:47.5139222Z 76 |         os.replace(temp_path, file_path)
2026-01-26T14:33:47.5139297Z 77 |     except Exception:
2026-01-26T14:33:47.5139357Z    |
2026-01-26T14:33:47.5139546Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5139558Z 
2026-01-26T14:33:47.5139689Z UP006 [*] Use `dict` instead of `Dict` for type annotation
2026-01-26T14:33:47.5139777Z   --> incremental_indexing.py:87:24
2026-01-26T14:33:47.5139836Z    |
2026-01-26T14:33:47.5139918Z 85 | class IndexMetadata:
2026-01-26T14:33:47.5139991Z 86 |     def __init__(self):
2026-01-26T14:33:47.5140090Z 87 |         self.metadata: Dict[str, Dict] = {}
2026-01-26T14:33:47.5140162Z    |                        ^^^^
2026-01-26T14:33:47.5140233Z 88 |         self.load()
2026-01-26T14:33:47.5140291Z    |
2026-01-26T14:33:47.5140366Z help: Replace with `dict`
2026-01-26T14:33:47.5140371Z 
2026-01-26T14:33:47.5140505Z UP006 [*] Use `dict` instead of `Dict` for type annotation
2026-01-26T14:33:47.5140599Z   --> incremental_indexing.py:87:34
2026-01-26T14:33:47.5140659Z    |
2026-01-26T14:33:47.5140744Z 85 | class IndexMetadata:
2026-01-26T14:33:47.5140815Z 86 |     def __init__(self):
2026-01-26T14:33:47.5140912Z 87 |         self.metadata: Dict[str, Dict] = {}
2026-01-26T14:33:47.5140986Z    |                                  ^^^^
2026-01-26T14:33:47.5141062Z 88 |         self.load()
2026-01-26T14:33:47.5141126Z    |
2026-01-26T14:33:47.5141214Z help: Replace with `dict`
2026-01-26T14:33:47.5141218Z 
2026-01-26T14:33:47.5141304Z UP015 [*] Unnecessary mode argument
2026-01-26T14:33:47.5141385Z   --> incremental_indexing.py:93:48
2026-01-26T14:33:47.5141443Z    |
2026-01-26T14:33:47.5141538Z 91 |         if INDEX_METADATA_FILE.exists():
2026-01-26T14:33:47.5141604Z 92 |             try:
2026-01-26T14:33:47.5141717Z 93 |                 with open(INDEX_METADATA_FILE, "r") as f:
2026-01-26T14:33:47.5141805Z    |                                                ^^^
2026-01-26T14:33:47.5141909Z 94 |                     self.metadata = json.load(f)
2026-01-26T14:33:47.5141987Z 95 |             except Exception:
2026-01-26T14:33:47.5142047Z    |
2026-01-26T14:33:47.5142128Z help: Remove mode argument
2026-01-26T14:33:47.5142132Z 
2026-01-26T14:33:47.5142219Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5142305Z    --> incremental_indexing.py:107:1
2026-01-26T14:33:47.5142370Z     |
2026-01-26T14:33:47.5142456Z 105 |         from logger import get_logger
2026-01-26T14:33:47.5142531Z 106 |         logger = get_logger()
2026-01-26T14:33:47.5142592Z 107 |         
2026-01-26T14:33:47.5142659Z     | ^^^^^^^^
2026-01-26T14:33:47.5142722Z 108 |         try:
2026-01-26T14:33:47.5142851Z 109 |             content = json.dumps(self.metadata, indent=2)
2026-01-26T14:33:47.5142915Z     |
2026-01-26T14:33:47.5143002Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5143007Z 
2026-01-26T14:33:47.5143130Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5143221Z    --> incremental_indexing.py:125:44
2026-01-26T14:33:47.5143287Z     |
2026-01-26T14:33:47.5143347Z 123 |         }
2026-01-26T14:33:47.5143405Z 124 |
2026-01-26T14:33:47.5143583Z 125 |     def get_changed_files(self, all_files: List[Path]) -> List[Path]:
2026-01-26T14:33:47.5143668Z     |                                            ^^^^
2026-01-26T14:33:47.5143742Z 126 |         changed_files = []
2026-01-26T14:33:47.5143806Z     |
2026-01-26T14:33:47.5143882Z help: Replace with `list`
2026-01-26T14:33:47.5143887Z 
2026-01-26T14:33:47.5144008Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5144096Z    --> incremental_indexing.py:125:59
2026-01-26T14:33:47.5144160Z     |
2026-01-26T14:33:47.5144221Z 123 |         }
2026-01-26T14:33:47.5144280Z 124 |
2026-01-26T14:33:47.5144445Z 125 |     def get_changed_files(self, all_files: List[Path]) -> List[Path]:
2026-01-26T14:33:47.5144548Z     |                                                           ^^^^
2026-01-26T14:33:47.5144757Z 126 |         changed_files = []
2026-01-26T14:33:47.5144816Z     |
2026-01-26T14:33:47.5144896Z help: Replace with `list`
2026-01-26T14:33:47.5144901Z 
2026-01-26T14:33:47.5145023Z UP006 [*] Use `set` instead of `Set` for type annotation
2026-01-26T14:33:47.5145180Z    --> incremental_indexing.py:140:52
2026-01-26T14:33:47.5145248Z     |
2026-01-26T14:33:47.5145329Z 138 |         return changed_files
2026-01-26T14:33:47.5145388Z 139 |
2026-01-26T14:33:47.5145556Z 140 |     def remove_deleted_files(self, existing_files: Set[str]) -> None:
2026-01-26T14:33:47.5145644Z     |                                                    ^^^
2026-01-26T14:33:47.5145718Z 141 |         files_to_remove = []
2026-01-26T14:33:47.5145823Z 142 |         for file_path in self.metadata.keys():
2026-01-26T14:33:47.5145888Z     |
2026-01-26T14:33:47.5145964Z help: Replace with `set`
2026-01-26T14:33:47.5145968Z 
2026-01-26T14:33:47.5146086Z UP006 [*] Use `dict` instead of `Dict` for type annotation
2026-01-26T14:33:47.5146179Z    --> incremental_indexing.py:149:28
2026-01-26T14:33:47.5146237Z     |
2026-01-26T14:33:47.5146330Z 147 |             del self.metadata[file_path]
2026-01-26T14:33:47.5146393Z 148 |
2026-01-26T14:33:47.5146475Z 149 |     def get_stats(self) -> Dict:
2026-01-26T14:33:47.5146545Z     |                            ^^^^
2026-01-26T14:33:47.5146624Z 150 |         if not self.metadata:
2026-01-26T14:33:47.5146748Z 151 |             return {"total_files": 0, "last_index": None}
2026-01-26T14:33:47.5146811Z     |
2026-01-26T14:33:47.5146887Z help: Replace with `dict`
2026-01-26T14:33:47.5146892Z 
2026-01-26T14:33:47.5147007Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5147076Z  --> logger.py:2:1
2026-01-26T14:33:47.5147135Z   |
2026-01-26T14:33:47.5147269Z 1 |   """Centralized logging configuration for ProjectMind"""
2026-01-26T14:33:47.5147342Z 2 | / import logging
2026-01-26T14:33:47.5147407Z 3 | | import sys
2026-01-26T14:33:47.5147527Z 4 | | from logging.handlers import RotatingFileHandler
2026-01-26T14:33:47.5147618Z 5 | | from pathlib import Path
2026-01-26T14:33:47.5147700Z 6 | | from typing import Optional
2026-01-26T14:33:47.5147759Z 7 | |
2026-01-26T14:33:47.5147930Z 8 | | from config import LOG_FILE, LOG_MAX_BYTES, LOG_BACKUP_COUNT, AI_DIR
2026-01-26T14:33:47.5148053Z   | |____________________________________________________________________^
2026-01-26T14:33:47.5148112Z   |
2026-01-26T14:33:47.5148185Z help: Organize imports
2026-01-26T14:33:47.5148191Z 
2026-01-26T14:33:47.5148293Z F401 [*] `pathlib.Path` imported but unused
2026-01-26T14:33:47.5148363Z  --> logger.py:5:21
2026-01-26T14:33:47.5148424Z   |
2026-01-26T14:33:47.5148492Z 3 | import sys
2026-01-26T14:33:47.5148610Z 4 | from logging.handlers import RotatingFileHandler
2026-01-26T14:33:47.5148688Z 5 | from pathlib import Path
2026-01-26T14:33:47.5148755Z   |                     ^^^^
2026-01-26T14:33:47.5148946Z 6 | from typing import Optional
2026-01-26T14:33:47.5149005Z   |
2026-01-26T14:33:47.5149102Z help: Remove unused import: `pathlib.Path`
2026-01-26T14:33:47.5149111Z 
2026-01-26T14:33:47.5149211Z UP045 [*] Use `X | None` for type annotations
2026-01-26T14:33:47.5149284Z   --> logger.py:11:10
2026-01-26T14:33:47.5149343Z    |
2026-01-26T14:33:47.5149446Z 11 | _logger: Optional[logging.Logger] = None
2026-01-26T14:33:47.5149517Z    |          ^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5149576Z    |
2026-01-26T14:33:47.5149652Z help: Convert to `X | None`
2026-01-26T14:33:47.5149657Z 
2026-01-26T14:33:47.5149744Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5149815Z   --> logger.py:17:1
2026-01-26T14:33:47.5149874Z    |
2026-01-26T14:33:47.5149939Z 15 |     """
2026-01-26T14:33:47.5150098Z 16 |     Sets up a rotating file logger with both file and stderr output.
2026-01-26T14:33:47.5150158Z 17 |     
2026-01-26T14:33:47.5150217Z    | ^^^^
2026-01-26T14:33:47.5150283Z 18 |     Args:
2026-01-26T14:33:47.5150355Z 19 |         name: Logger name
2026-01-26T14:33:47.5150413Z    |
2026-01-26T14:33:47.5150635Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5150641Z 
2026-01-26T14:33:47.5150721Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5150794Z   --> logger.py:20:1
2026-01-26T14:33:47.5150859Z    |
2026-01-26T14:33:47.5150920Z 18 |     Args:
2026-01-26T14:33:47.5151091Z 19 |         name: Logger name
2026-01-26T14:33:47.5151154Z 20 |         
2026-01-26T14:33:47.5151219Z    | ^^^^^^^^
2026-01-26T14:33:47.5151282Z 21 |     Returns:
2026-01-26T14:33:47.5151365Z 22 |         Configured logger instance
2026-01-26T14:33:47.5151428Z    |
2026-01-26T14:33:47.5151514Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5151519Z 
2026-01-26T14:33:47.5151600Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5151669Z   --> logger.py:25:1
2026-01-26T14:33:47.5151732Z    |
2026-01-26T14:33:47.5151791Z 23 |     """
2026-01-26T14:33:47.5151863Z 24 |     global _logger
2026-01-26T14:33:47.5151927Z 25 |     
2026-01-26T14:33:47.5151985Z    | ^^^^
2026-01-26T14:33:47.5152061Z 26 |     if _logger is not None:
2026-01-26T14:33:47.5152135Z 27 |         return _logger
2026-01-26T14:33:47.5152200Z    |
2026-01-26T14:33:47.5152285Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5152289Z 
2026-01-26T14:33:47.5152373Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5152448Z   --> logger.py:28:1
2026-01-26T14:33:47.5152507Z    |
2026-01-26T14:33:47.5152582Z 26 |     if _logger is not None:
2026-01-26T14:33:47.5152652Z 27 |         return _logger
2026-01-26T14:33:47.5152718Z 28 |     
2026-01-26T14:33:47.5152776Z    | ^^^^
2026-01-26T14:33:47.5152865Z 29 |     logger = logging.getLogger(name)
2026-01-26T14:33:47.5152959Z 30 |     logger.setLevel(logging.INFO)
2026-01-26T14:33:47.5153021Z    |
2026-01-26T14:33:47.5153109Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5153114Z 
2026-01-26T14:33:47.5153198Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5153268Z   --> logger.py:31:1
2026-01-26T14:33:47.5153326Z    |
2026-01-26T14:33:47.5153418Z 29 |     logger = logging.getLogger(name)
2026-01-26T14:33:47.5153508Z 30 |     logger.setLevel(logging.INFO)
2026-01-26T14:33:47.5153570Z 31 |     
2026-01-26T14:33:47.5153629Z    | ^^^^
2026-01-26T14:33:47.5153714Z 32 |     logger.handlers.clear()
2026-01-26T14:33:47.5153774Z    |
2026-01-26T14:33:47.5153858Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5153863Z 
2026-01-26T14:33:47.5153944Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5154018Z   --> logger.py:33:1
2026-01-26T14:33:47.5154075Z    |
2026-01-26T14:33:47.5154153Z 32 |     logger.handlers.clear()
2026-01-26T14:33:47.5154223Z 33 |     
2026-01-26T14:33:47.5154282Z    | ^^^^
2026-01-26T14:33:47.5154366Z 34 |     formatter = logging.Formatter(
2026-01-26T14:33:47.5154570Z 35 |         fmt='[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
2026-01-26T14:33:47.5154636Z    |
2026-01-26T14:33:47.5154721Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5154726Z 
2026-01-26T14:33:47.5154810Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5154890Z   --> logger.py:38:1
2026-01-26T14:33:47.5154949Z    |
2026-01-26T14:33:47.5155029Z 36 |         datefmt='%Y-%m-%d %H:%M:%S'
2026-01-26T14:33:47.5155096Z 37 |     )
2026-01-26T14:33:47.5155159Z 38 |     
2026-01-26T14:33:47.5155218Z    | ^^^^
2026-01-26T14:33:47.5155279Z 39 |     try:
2026-01-26T14:33:47.5155393Z 40 |         AI_DIR.mkdir(parents=True, exist_ok=True)
2026-01-26T14:33:47.5155452Z    |
2026-01-26T14:33:47.5155538Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5155544Z 
2026-01-26T14:33:47.5155631Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5155699Z   --> logger.py:41:1
2026-01-26T14:33:47.5155757Z    |
2026-01-26T14:33:47.5155818Z 39 |     try:
2026-01-26T14:33:47.5155926Z 40 |         AI_DIR.mkdir(parents=True, exist_ok=True)
2026-01-26T14:33:47.5155987Z 41 |         
2026-01-26T14:33:47.5156046Z    | ^^^^^^^^
2026-01-26T14:33:47.5156151Z 42 |         file_handler = RotatingFileHandler(
2026-01-26T14:33:47.5156311Z 43 |             LOG_FILE,
2026-01-26T14:33:47.5156377Z    |
2026-01-26T14:33:47.5164067Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5164700Z 
2026-01-26T14:33:47.5164884Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5165214Z   --> logger.py:53:1
2026-01-26T14:33:47.5165333Z    |
2026-01-26T14:33:47.5165465Z 51 |     except Exception as e:
2026-01-26T14:33:47.5165733Z 52 |         sys.stderr.write(f"Warning: Could not setup file logging: {e}\n")
2026-01-26T14:33:47.5165929Z 53 |     
2026-01-26T14:33:47.5166025Z    | ^^^^
2026-01-26T14:33:47.5166231Z 54 |     stderr_handler = logging.StreamHandler(sys.stderr)
2026-01-26T14:33:47.5166390Z 55 |     stderr_handler.setLevel(logging.WARNING)
2026-01-26T14:33:47.5166481Z    |
2026-01-26T14:33:47.5166622Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5166631Z 
2026-01-26T14:33:47.5166757Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5166867Z   --> logger.py:58:1
2026-01-26T14:33:47.5166975Z    |
2026-01-26T14:33:47.5167130Z 56 |     stderr_handler.setFormatter(formatter)
2026-01-26T14:33:47.5167270Z 57 |     logger.addHandler(stderr_handler)
2026-01-26T14:33:47.5167362Z 58 |     
2026-01-26T14:33:47.5167461Z    | ^^^^
2026-01-26T14:33:47.5167574Z 59 |     _logger = logger
2026-01-26T14:33:47.5167681Z 60 |     return logger
2026-01-26T14:33:47.5167778Z    |
2026-01-26T14:33:47.5167987Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5167996Z 
2026-01-26T14:33:47.5168119Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5168241Z   --> logger.py:67:1
2026-01-26T14:33:47.5168391Z    |
2026-01-26T14:33:47.5168562Z 65 |     Gets the configured logger instance.
2026-01-26T14:33:47.5168714Z 66 |     Creates it if it doesn't exist.
2026-01-26T14:33:47.5168981Z 67 |     
2026-01-26T14:33:47.5169094Z    | ^^^^
2026-01-26T14:33:47.5169202Z 68 |     Returns:
2026-01-26T14:33:47.5169327Z 69 |         Logger instance
2026-01-26T14:33:47.5169436Z    |
2026-01-26T14:33:47.5169598Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5169606Z 
2026-01-26T14:33:47.5169768Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5169892Z   --> mcp_server.py:1:1
2026-01-26T14:33:47.5169983Z    |
2026-01-26T14:33:47.5170090Z  1 | / import os
2026-01-26T14:33:47.5170188Z  2 | | import sys
2026-01-26T14:33:47.5170294Z  3 | | import json
2026-01-26T14:33:47.5170399Z  4 | | import shutil
2026-01-26T14:33:47.5170528Z  5 | | from pathlib import Path
2026-01-26T14:33:47.5170710Z  6 | | from typing import List, Optional, Set, Dict
2026-01-26T14:33:47.5170858Z  7 | | from mcp.server.fastmcp import FastMCP
2026-01-26T14:33:47.5170962Z  8 | | import git
2026-01-26T14:33:47.5171121Z  9 | | from datetime import datetime, timedelta
2026-01-26T14:33:47.5171213Z 10 | |
2026-01-26T14:33:47.5171330Z 11 | | from config import (
2026-01-26T14:33:47.5171432Z 12 | |     AI_DIR,
2026-01-26T14:33:47.5171551Z 13 | |     MEMORY_FILE,
2026-01-26T14:33:47.5171668Z 14 | |     VECTOR_STORE_DIR,
2026-01-26T14:33:47.5171789Z 15 | |     INDEX_IGNORE_FILE,
2026-01-26T14:33:47.5171908Z 16 | |     INDEX_METADATA_FILE,
2026-01-26T14:33:47.5172025Z 17 | |     MEMORY_HISTORY_DIR,
2026-01-26T14:33:47.5172132Z 18 | |     MODEL_NAME,
2026-01-26T14:33:47.5172237Z 19 | |     CHUNK_SIZE,
2026-01-26T14:33:47.5172358Z 20 | |     CHUNK_OVERLAP,
2026-01-26T14:33:47.5172466Z 21 | |     BATCH_SIZE,
2026-01-26T14:33:47.5172574Z 22 | |     BINARY_EXTENSIONS,
2026-01-26T14:33:47.5172709Z 23 | |     INDEXABLE_EXTENSIONS,
2026-01-26T14:33:47.5172835Z 24 | |     get_max_file_size_bytes,
2026-01-26T14:33:47.5172952Z 25 | |     get_max_memory_bytes,
2026-01-26T14:33:47.5173063Z 26 | |     get_ignored_dirs,
2026-01-26T14:33:47.5173177Z 27 | |     validate_path,
2026-01-26T14:33:47.5173290Z 28 | |     safe_read_text,
2026-01-26T14:33:47.5173405Z 29 | |     get_file_cache_stats,
2026-01-26T14:33:47.5173503Z 30 | | )
2026-01-26T14:33:47.5173683Z 31 | | from incremental_indexing import IndexMetadata
2026-01-26T14:33:47.5173916Z 32 | | from memory_limited_indexer import MemoryLimitedIndexer
2026-01-26T14:33:47.5174355Z 33 | | from vector_store_manager import VectorStoreManager
2026-01-26T14:33:47.5174540Z 34 | | from memory_manager import MemoryManager
2026-01-26T14:33:47.5174871Z 35 | | from codebase_indexer import CodebaseIndexer
2026-01-26T14:33:47.5175061Z 36 | | from logger import setup_logger, get_logger
2026-01-26T14:33:47.5175195Z    | |___________________________________________^
2026-01-26T14:33:47.5175287Z 37 |
2026-01-26T14:33:47.5175406Z 38 |   logger = setup_logger()
2026-01-26T14:33:47.5175507Z    |
2026-01-26T14:33:47.5175619Z help: Organize imports
2026-01-26T14:33:47.5175627Z 
2026-01-26T14:33:47.5175746Z F401 [*] `json` imported but unused
2026-01-26T14:33:47.5175860Z  --> mcp_server.py:3:8
2026-01-26T14:33:47.5175964Z   |
2026-01-26T14:33:47.5176070Z 1 | import os
2026-01-26T14:33:47.5176172Z 2 | import sys
2026-01-26T14:33:47.5176284Z 3 | import json
2026-01-26T14:33:47.5176381Z   |        ^^^^
2026-01-26T14:33:47.5176502Z 4 | import shutil
2026-01-26T14:33:47.5176628Z 5 | from pathlib import Path
2026-01-26T14:33:47.5176729Z   |
2026-01-26T14:33:47.5176864Z help: Remove unused import: `json`
2026-01-26T14:33:47.5176871Z 
2026-01-26T14:33:47.5177006Z F401 [*] `shutil` imported but unused
2026-01-26T14:33:47.5177142Z  --> mcp_server.py:4:8
2026-01-26T14:33:47.5177245Z   |
2026-01-26T14:33:47.5177354Z 2 | import sys
2026-01-26T14:33:47.5177467Z 3 | import json
2026-01-26T14:33:47.5177588Z 4 | import shutil
2026-01-26T14:33:47.5177692Z   |        ^^^^^^
2026-01-26T14:33:47.5177824Z 5 | from pathlib import Path
2026-01-26T14:33:47.5178023Z 6 | from typing import List, Optional, Set, Dict
2026-01-26T14:33:47.5178127Z   |
2026-01-26T14:33:47.5178272Z help: Remove unused import: `shutil`
2026-01-26T14:33:47.5178280Z 
2026-01-26T14:33:47.5178503Z UP035 `typing.List` is deprecated, use `list` instead
2026-01-26T14:33:47.5178635Z  --> mcp_server.py:6:1
2026-01-26T14:33:47.5178737Z   |
2026-01-26T14:33:47.5179063Z 4 | import shutil
2026-01-26T14:33:47.5179226Z 5 | from pathlib import Path
2026-01-26T14:33:47.5179409Z 6 | from typing import List, Optional, Set, Dict
2026-01-26T14:33:47.5179545Z   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5179721Z 7 | from mcp.server.fastmcp import FastMCP
2026-01-26T14:33:47.5179833Z 8 | import git
2026-01-26T14:33:47.5179931Z   |
2026-01-26T14:33:47.5179940Z 
2026-01-26T14:33:47.5180138Z UP035 `typing.Set` is deprecated, use `set` instead
2026-01-26T14:33:47.5180279Z  --> mcp_server.py:6:1
2026-01-26T14:33:47.5180384Z   |
2026-01-26T14:33:47.5180498Z 4 | import shutil
2026-01-26T14:33:47.5180645Z 5 | from pathlib import Path
2026-01-26T14:33:47.5180829Z 6 | from typing import List, Optional, Set, Dict
2026-01-26T14:33:47.5180962Z   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5181135Z 7 | from mcp.server.fastmcp import FastMCP
2026-01-26T14:33:47.5181250Z 8 | import git
2026-01-26T14:33:47.5181353Z   |
2026-01-26T14:33:47.5181362Z 
2026-01-26T14:33:47.5181580Z UP035 `typing.Dict` is deprecated, use `dict` instead
2026-01-26T14:33:47.5181715Z  --> mcp_server.py:6:1
2026-01-26T14:33:47.5181812Z   |
2026-01-26T14:33:47.5181916Z 4 | import shutil
2026-01-26T14:33:47.5182057Z 5 | from pathlib import Path
2026-01-26T14:33:47.5182244Z 6 | from typing import List, Optional, Set, Dict
2026-01-26T14:33:47.5182381Z   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5182545Z 7 | from mcp.server.fastmcp import FastMCP
2026-01-26T14:33:47.5182662Z 8 | import git
2026-01-26T14:33:47.5182750Z   |
2026-01-26T14:33:47.5182758Z 
2026-01-26T14:33:47.5182896Z F401 [*] `typing.Dict` imported but unused
2026-01-26T14:33:47.5183019Z  --> mcp_server.py:6:41
2026-01-26T14:33:47.5183117Z   |
2026-01-26T14:33:47.5183218Z 4 | import shutil
2026-01-26T14:33:47.5183350Z 5 | from pathlib import Path
2026-01-26T14:33:47.5183504Z 6 | from typing import List, Optional, Set, Dict
2026-01-26T14:33:47.5183620Z   |                                         ^^^^
2026-01-26T14:33:47.5183996Z 7 | from mcp.server.fastmcp import FastMCP
2026-01-26T14:33:47.5184109Z 8 | import git
2026-01-26T14:33:47.5184202Z   |
2026-01-26T14:33:47.5184380Z help: Remove unused import: `typing.Dict`
2026-01-26T14:33:47.5184389Z 
2026-01-26T14:33:47.5184769Z F401 [*] `config.VECTOR_STORE_DIR` imported but unused
2026-01-26T14:33:47.5184902Z   --> mcp_server.py:14:5
2026-01-26T14:33:47.5185004Z    |
2026-01-26T14:33:47.5185102Z 12 |     AI_DIR,
2026-01-26T14:33:47.5185213Z 13 |     MEMORY_FILE,
2026-01-26T14:33:47.5185324Z 14 |     VECTOR_STORE_DIR,
2026-01-26T14:33:47.5185426Z    |     ^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5185549Z 15 |     INDEX_IGNORE_FILE,
2026-01-26T14:33:47.5185671Z 16 |     INDEX_METADATA_FILE,
2026-01-26T14:33:47.5185776Z    |
2026-01-26T14:33:47.5185903Z help: Remove unused import
2026-01-26T14:33:47.5185918Z 
2026-01-26T14:33:47.5186115Z F401 [*] `config.INDEX_METADATA_FILE` imported but unused
2026-01-26T14:33:47.5186235Z   --> mcp_server.py:16:5
2026-01-26T14:33:47.5186327Z    |
2026-01-26T14:33:47.5186454Z 14 |     VECTOR_STORE_DIR,
2026-01-26T14:33:47.5186569Z 15 |     INDEX_IGNORE_FILE,
2026-01-26T14:33:47.5186687Z 16 |     INDEX_METADATA_FILE,
2026-01-26T14:33:47.5186794Z    |     ^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5186918Z 17 |     MEMORY_HISTORY_DIR,
2026-01-26T14:33:47.5187024Z 18 |     MODEL_NAME,
2026-01-26T14:33:47.5187123Z    |
2026-01-26T14:33:47.5187261Z help: Remove unused import
2026-01-26T14:33:47.5187269Z 
2026-01-26T14:33:47.5187470Z F401 [*] `config.MEMORY_HISTORY_DIR` imported but unused
2026-01-26T14:33:47.5187592Z   --> mcp_server.py:17:5
2026-01-26T14:33:47.5187690Z    |
2026-01-26T14:33:47.5187807Z 15 |     INDEX_IGNORE_FILE,
2026-01-26T14:33:47.5187933Z 16 |     INDEX_METADATA_FILE,
2026-01-26T14:33:47.5188063Z 17 |     MEMORY_HISTORY_DIR,
2026-01-26T14:33:47.5189398Z    |     ^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5189548Z 18 |     MODEL_NAME,
2026-01-26T14:33:47.5189652Z 19 |     CHUNK_SIZE,
2026-01-26T14:33:47.5189753Z    |
2026-01-26T14:33:47.5189877Z help: Remove unused import
2026-01-26T14:33:47.5189897Z 
2026-01-26T14:33:47.5190077Z F401 [*] `config.MODEL_NAME` imported but unused
2026-01-26T14:33:47.5190220Z   --> mcp_server.py:18:5
2026-01-26T14:33:47.5190326Z    |
2026-01-26T14:33:47.5190455Z 16 |     INDEX_METADATA_FILE,
2026-01-26T14:33:47.5190580Z 17 |     MEMORY_HISTORY_DIR,
2026-01-26T14:33:47.5190689Z 18 |     MODEL_NAME,
2026-01-26T14:33:47.5190790Z    |     ^^^^^^^^^^
2026-01-26T14:33:47.5190901Z 19 |     CHUNK_SIZE,
2026-01-26T14:33:47.5191026Z 20 |     CHUNK_OVERLAP,
2026-01-26T14:33:47.5191125Z    |
2026-01-26T14:33:47.5191263Z help: Remove unused import
2026-01-26T14:33:47.5191272Z 
2026-01-26T14:33:47.5191446Z F401 [*] `config.CHUNK_SIZE` imported but unused
2026-01-26T14:33:47.5191595Z   --> mcp_server.py:19:5
2026-01-26T14:33:47.5191699Z    |
2026-01-26T14:33:47.5191828Z 17 |     MEMORY_HISTORY_DIR,
2026-01-26T14:33:47.5191955Z 18 |     MODEL_NAME,
2026-01-26T14:33:47.5192070Z 19 |     CHUNK_SIZE,
2026-01-26T14:33:47.5192178Z    |     ^^^^^^^^^^
2026-01-26T14:33:47.5192316Z 20 |     CHUNK_OVERLAP,
2026-01-26T14:33:47.5192445Z 21 |     BATCH_SIZE,
2026-01-26T14:33:47.5192552Z    |
2026-01-26T14:33:47.5192689Z help: Remove unused import
2026-01-26T14:33:47.5192699Z 
2026-01-26T14:33:47.5192919Z F401 [*] `config.CHUNK_OVERLAP` imported but unused
2026-01-26T14:33:47.5193109Z   --> mcp_server.py:20:5
2026-01-26T14:33:47.5193177Z    |
2026-01-26T14:33:47.5193247Z 18 |     MODEL_NAME,
2026-01-26T14:33:47.5193321Z 19 |     CHUNK_SIZE,
2026-01-26T14:33:47.5193392Z 20 |     CHUNK_OVERLAP,
2026-01-26T14:33:47.5193456Z    |     ^^^^^^^^^^^^^
2026-01-26T14:33:47.5193526Z 21 |     BATCH_SIZE,
2026-01-26T14:33:47.5193601Z 22 |     BINARY_EXTENSIONS,
2026-01-26T14:33:47.5193662Z    |
2026-01-26T14:33:47.5193740Z help: Remove unused import
2026-01-26T14:33:47.5193753Z 
2026-01-26T14:33:47.5193866Z F401 [*] `config.BATCH_SIZE` imported but unused
2026-01-26T14:33:47.5193948Z   --> mcp_server.py:21:5
2026-01-26T14:33:47.5194007Z    |
2026-01-26T14:33:47.5194285Z 19 |     CHUNK_SIZE,
2026-01-26T14:33:47.5194358Z 20 |     CHUNK_OVERLAP,
2026-01-26T14:33:47.5194424Z 21 |     BATCH_SIZE,
2026-01-26T14:33:47.5194493Z    |     ^^^^^^^^^^
2026-01-26T14:33:47.5194567Z 22 |     BINARY_EXTENSIONS,
2026-01-26T14:33:47.5194762Z 23 |     INDEXABLE_EXTENSIONS,
2026-01-26T14:33:47.5194826Z    |
2026-01-26T14:33:47.5194909Z help: Remove unused import
2026-01-26T14:33:47.5194914Z 
2026-01-26T14:33:47.5195045Z F401 [*] `config.BINARY_EXTENSIONS` imported but unused
2026-01-26T14:33:47.5195123Z   --> mcp_server.py:22:5
2026-01-26T14:33:47.5195198Z    |
2026-01-26T14:33:47.5195270Z 20 |     CHUNK_OVERLAP,
2026-01-26T14:33:47.5195339Z 21 |     BATCH_SIZE,
2026-01-26T14:33:47.5195413Z 22 |     BINARY_EXTENSIONS,
2026-01-26T14:33:47.5195483Z    |     ^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5195570Z 23 |     INDEXABLE_EXTENSIONS,
2026-01-26T14:33:47.5195730Z 24 |     get_max_file_size_bytes,
2026-01-26T14:33:47.5195804Z    |
2026-01-26T14:33:47.5195884Z help: Remove unused import
2026-01-26T14:33:47.5195894Z 
2026-01-26T14:33:47.5196028Z F401 [*] `config.INDEXABLE_EXTENSIONS` imported but unused
2026-01-26T14:33:47.5196110Z   --> mcp_server.py:23:5
2026-01-26T14:33:47.5196171Z    |
2026-01-26T14:33:47.5196238Z 21 |     BATCH_SIZE,
2026-01-26T14:33:47.5196317Z 22 |     BINARY_EXTENSIONS,
2026-01-26T14:33:47.5196399Z 23 |     INDEXABLE_EXTENSIONS,
2026-01-26T14:33:47.5196469Z    |     ^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5196546Z 24 |     get_max_file_size_bytes,
2026-01-26T14:33:47.5196625Z 25 |     get_max_memory_bytes,
2026-01-26T14:33:47.5196685Z    |
2026-01-26T14:33:47.5196762Z help: Remove unused import
2026-01-26T14:33:47.5196767Z 
2026-01-26T14:33:47.5196903Z F401 [*] `config.get_max_file_size_bytes` imported but unused
2026-01-26T14:33:47.5196983Z   --> mcp_server.py:24:5
2026-01-26T14:33:47.5197043Z    |
2026-01-26T14:33:47.5197115Z 22 |     BINARY_EXTENSIONS,
2026-01-26T14:33:47.5197195Z 23 |     INDEXABLE_EXTENSIONS,
2026-01-26T14:33:47.5197271Z 24 |     get_max_file_size_bytes,
2026-01-26T14:33:47.5197345Z    |     ^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5197419Z 25 |     get_max_memory_bytes,
2026-01-26T14:33:47.5197496Z 26 |     get_ignored_dirs,
2026-01-26T14:33:47.5197556Z    |
2026-01-26T14:33:47.5197632Z help: Remove unused import
2026-01-26T14:33:47.5197640Z 
2026-01-26T14:33:47.5197770Z F401 [*] `config.get_max_memory_bytes` imported but unused
2026-01-26T14:33:47.5197844Z   --> mcp_server.py:25:5
2026-01-26T14:33:47.5197903Z    |
2026-01-26T14:33:47.5197981Z 23 |     INDEXABLE_EXTENSIONS,
2026-01-26T14:33:47.5198056Z 24 |     get_max_file_size_bytes,
2026-01-26T14:33:47.5198130Z 25 |     get_max_memory_bytes,
2026-01-26T14:33:47.5198198Z    |     ^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5198275Z 26 |     get_ignored_dirs,
2026-01-26T14:33:47.5198345Z 27 |     validate_path,
2026-01-26T14:33:47.5198404Z    |
2026-01-26T14:33:47.5198487Z help: Remove unused import
2026-01-26T14:33:47.5198492Z 
2026-01-26T14:33:47.5198603Z F401 [*] `config.safe_read_text` imported but unused
2026-01-26T14:33:47.5198680Z   --> mcp_server.py:28:5
2026-01-26T14:33:47.5198740Z    |
2026-01-26T14:33:47.5199089Z 26 |     get_ignored_dirs,
2026-01-26T14:33:47.5199167Z 27 |     validate_path,
2026-01-26T14:33:47.5199237Z 28 |     safe_read_text,
2026-01-26T14:33:47.5199312Z    |     ^^^^^^^^^^^^^^
2026-01-26T14:33:47.5199386Z 29 |     get_file_cache_stats,
2026-01-26T14:33:47.5199448Z 30 | )
2026-01-26T14:33:47.5199508Z    |
2026-01-26T14:33:47.5199590Z help: Remove unused import
2026-01-26T14:33:47.5199595Z 
2026-01-26T14:33:47.5199748Z F401 [*] `incremental_indexing.IndexMetadata` imported but unused
2026-01-26T14:33:47.5199827Z   --> mcp_server.py:31:34
2026-01-26T14:33:47.5199895Z    |
2026-01-26T14:33:47.5199967Z 29 |     get_file_cache_stats,
2026-01-26T14:33:47.5200027Z 30 | )
2026-01-26T14:33:47.5200147Z 31 | from incremental_indexing import IndexMetadata
2026-01-26T14:33:47.5200227Z    |                                  ^^^^^^^^^^^^^
2026-01-26T14:33:47.5200363Z 32 | from memory_limited_indexer import MemoryLimitedIndexer
2026-01-26T14:33:47.5200637Z 33 | from vector_store_manager import VectorStoreManager
2026-01-26T14:33:47.5200703Z    |
2026-01-26T14:33:47.5200868Z help: Remove unused import: `incremental_indexing.IndexMetadata`
2026-01-26T14:33:47.5200873Z 
2026-01-26T14:33:47.5201157Z F401 [*] `memory_limited_indexer.MemoryLimitedIndexer` imported but unused
2026-01-26T14:33:47.5201249Z   --> mcp_server.py:32:36
2026-01-26T14:33:47.5201310Z    |
2026-01-26T14:33:47.5201370Z 30 | )
2026-01-26T14:33:47.5201497Z 31 | from incremental_indexing import IndexMetadata
2026-01-26T14:33:47.5201633Z 32 | from memory_limited_indexer import MemoryLimitedIndexer
2026-01-26T14:33:47.5201724Z    |                                    ^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5201846Z 33 | from vector_store_manager import VectorStoreManager
2026-01-26T14:33:47.5201954Z 34 | from memory_manager import MemoryManager
2026-01-26T14:33:47.5202014Z    |
2026-01-26T14:33:47.5202198Z help: Remove unused import: `memory_limited_indexer.MemoryLimitedIndexer`
2026-01-26T14:33:47.5202208Z 
2026-01-26T14:33:47.5202318Z F401 [*] `logger.get_logger` imported but unused
2026-01-26T14:33:47.5202395Z   --> mcp_server.py:36:34
2026-01-26T14:33:47.5202453Z    |
2026-01-26T14:33:47.5202554Z 34 | from memory_manager import MemoryManager
2026-01-26T14:33:47.5202658Z 35 | from codebase_indexer import CodebaseIndexer
2026-01-26T14:33:47.5202754Z 36 | from logger import setup_logger, get_logger
2026-01-26T14:33:47.5202830Z    |                                  ^^^^^^^^^^
2026-01-26T14:33:47.5202896Z 37 |
2026-01-26T14:33:47.5202975Z 38 | logger = setup_logger()
2026-01-26T14:33:47.5203037Z    |
2026-01-26T14:33:47.5203151Z help: Remove unused import: `logger.get_logger`
2026-01-26T14:33:47.5203156Z 
2026-01-26T14:33:47.5203258Z C901 `startup_check` is too complex (13 > 10)
2026-01-26T14:33:47.5203335Z   --> mcp_server.py:50:5
2026-01-26T14:33:47.5203393Z    |
2026-01-26T14:33:47.5203487Z 50 | def startup_check() -> None:
2026-01-26T14:33:47.5203560Z    |     ^^^^^^^^^^^^^
2026-01-26T14:33:47.5203685Z 51 |     log(f"Running startup check in {os.getcwd()}...")
2026-01-26T14:33:47.5203751Z    |
2026-01-26T14:33:47.5203755Z 
2026-01-26T14:33:47.5203833Z W291 Trailing whitespace
2026-01-26T14:33:47.5203916Z    --> mcp_server.py:98:13
2026-01-26T14:33:47.5203983Z     |
2026-01-26T14:33:47.5204048Z  96 | ## Tech Stack
2026-01-26T14:33:47.5204142Z  97 | - Language: Python
2026-01-26T14:33:47.5204216Z  98 | - Framework: 
2026-01-26T14:33:47.5204285Z     |             ^
2026-01-26T14:33:47.5204346Z  99 |
2026-01-26T14:33:47.5204420Z 100 | ## Recent Decisions
2026-01-26T14:33:47.5204485Z     |
2026-01-26T14:33:47.5204572Z help: Remove trailing whitespace
2026-01-26T14:33:47.5204578Z 
2026-01-26T14:33:47.5204702Z UP006 [*] Use `set` instead of `Set` for type annotation
2026-01-26T14:33:47.5204786Z    --> mcp_server.py:117:37
2026-01-26T14:33:47.5204852Z     |
2026-01-26T14:33:47.5204971Z 117 | def load_index_ignore_patterns() -> Set[str]:
2026-01-26T14:33:47.5205053Z     |                                     ^^^
2026-01-26T14:33:47.5205155Z 118 |     if not INDEX_IGNORE_FILE.exists():
2026-01-26T14:33:47.5205226Z 119 |         return set()
2026-01-26T14:33:47.5205286Z     |
2026-01-26T14:33:47.5205366Z help: Replace with `set`
2026-01-26T14:33:47.5205377Z 
2026-01-26T14:33:47.5205463Z UP015 [*] Unnecessary mode argument
2026-01-26T14:33:47.5205540Z    --> mcp_server.py:123:38
2026-01-26T14:33:47.5205600Z     |
2026-01-26T14:33:47.5205670Z 121 |     try:
2026-01-26T14:33:47.5205748Z 122 |         patterns = set()
2026-01-26T14:33:47.5205859Z 123 |         with open(INDEX_IGNORE_FILE, "r") as f:
2026-01-26T14:33:47.5205944Z     |                                      ^^^
2026-01-26T14:33:47.5206019Z 124 |             for line in f:
2026-01-26T14:33:47.5206104Z 125 |                 line = line.strip()
2026-01-26T14:33:47.5206164Z     |
2026-01-26T14:33:47.5206247Z help: Remove mode argument
2026-01-26T14:33:47.5206252Z 
2026-01-26T14:33:47.5206339Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5206513Z    --> mcp_server.py:166:1
2026-01-26T14:33:47.5206579Z     |
2026-01-26T14:33:47.5206684Z 164 |     if vector_store.get_collection() is None:
2026-01-26T14:33:47.5206885Z 165 |         return "Failed to initialize vector store."
2026-01-26T14:33:47.5206960Z 166 |     
2026-01-26T14:33:47.5207022Z     | ^^^^
2026-01-26T14:33:47.5207101Z 167 |     root_dir = Path(".")
2026-01-26T14:33:47.5207202Z 168 |     ignored_dirs = get_ignored_dirs()
2026-01-26T14:33:47.5207265Z     |
2026-01-26T14:33:47.5207354Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5207360Z 
2026-01-26T14:33:47.5207443Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5207524Z    --> mcp_server.py:170:1
2026-01-26T14:33:47.5207584Z     |
2026-01-26T14:33:47.5207670Z 168 |     ignored_dirs = get_ignored_dirs()
2026-01-26T14:33:47.5207789Z 169 |     ignore_patterns = load_index_ignore_patterns()
2026-01-26T14:33:47.5207856Z 170 |     
2026-01-26T14:33:47.5207918Z     | ^^^^
2026-01-26T14:33:47.5208129Z 171 |     return indexer.index_all(root_dir, ignored_dirs, ignore_patterns, force)
2026-01-26T14:33:47.5208195Z     |
2026-01-26T14:33:47.5208284Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5208289Z 
2026-01-26T14:33:47.5208384Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5208465Z    --> mcp_server.py:187:1
2026-01-26T14:33:47.5208525Z     |
2026-01-26T14:33:47.5208589Z 185 |     try:
2026-01-26T14:33:47.5209085Z 186 |         results = vector_store.query(query_texts=[query], n_results=n_results)
2026-01-26T14:33:47.5209214Z 187 |         
2026-01-26T14:33:47.5209319Z     | ^^^^^^^^
2026-01-26T14:33:47.5209450Z 188 |         if results is None:
2026-01-26T14:33:47.5209662Z 189 |             return "Vector store not initialized."
2026-01-26T14:33:47.5209763Z     |
2026-01-26T14:33:47.5209917Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5209927Z 
2026-01-26T14:33:47.5210115Z C901 `ingest_git_history` is too complex (12 > 10)
2026-01-26T14:33:47.5210266Z    --> mcp_server.py:206:5
2026-01-26T14:33:47.5210366Z     |
2026-01-26T14:33:47.5210481Z 205 | @mcp.tool()
2026-01-26T14:33:47.5210683Z 206 | def ingest_git_history(limit: int = 30) -> str:
2026-01-26T14:33:47.5210813Z     |     ^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5210948Z 207 |     if limit <= 0:
2026-01-26T14:33:47.5211156Z 208 |         return "Error: Limit must be greater than 0."
2026-01-26T14:33:47.5211265Z     |
2026-01-26T14:33:47.5211272Z 
2026-01-26T14:33:47.5211422Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5211560Z    --> mcp_server.py:274:1
2026-01-26T14:33:47.5211675Z     |
2026-01-26T14:33:47.5211789Z 272 |     try:
2026-01-26T14:33:47.5211921Z 273 |         summary_parts = []
2026-01-26T14:33:47.5212042Z 274 |         
2026-01-26T14:33:47.5212108Z     | ^^^^^^^^
2026-01-26T14:33:47.5212241Z 275 |         summary_parts.append("# PROJECT SUMMARY\n")
2026-01-26T14:33:47.5212302Z     |
2026-01-26T14:33:47.5212399Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5212411Z 
2026-01-26T14:33:47.5212496Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5212577Z    --> mcp_server.py:276:1
2026-01-26T14:33:47.5212648Z     |
2026-01-26T14:33:47.5212766Z 275 |         summary_parts.append("# PROJECT SUMMARY\n")
2026-01-26T14:33:47.5212829Z 276 |         
2026-01-26T14:33:47.5212890Z     | ^^^^^^^^
2026-01-26T14:33:47.5212975Z 277 |         memory = read_memory()
2026-01-26T14:33:47.5213112Z 278 |         if memory and "Memory file not found" not in memory:
2026-01-26T14:33:47.5213172Z     |
2026-01-26T14:33:47.5213266Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5213271Z 
2026-01-26T14:33:47.5213354Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5213431Z    --> mcp_server.py:284:1
2026-01-26T14:33:47.5213496Z     |
2026-01-26T14:33:47.5213597Z 282 |             if len(memory.split('\n')) > 30:
2026-01-26T14:33:47.5213769Z 283 |                 summary_parts.append("\n... (truncated, see full memory)\n")
2026-01-26T14:33:47.5213998Z 284 |         
2026-01-26T14:33:47.5214065Z     | ^^^^^^^^
2026-01-26T14:33:47.5214129Z 285 |         try:
2026-01-26T14:33:47.5214290Z 286 |             repo = git.Repo(os.getcwd(), search_parent_directories=True)
2026-01-26T14:33:47.5214357Z     |
2026-01-26T14:33:47.5214548Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5214554Z 
2026-01-26T14:33:47.5214638Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5214721Z    --> mcp_server.py:296:1
2026-01-26T14:33:47.5214780Z     |
2026-01-26T14:33:47.5214858Z 294 |         except Exception:
2026-01-26T14:33:47.5214934Z 295 |             pass
2026-01-26T14:33:47.5215001Z 296 |         
2026-01-26T14:33:47.5215062Z     | ^^^^^^^^
2026-01-26T14:33:47.5215141Z 297 |         root = Path(".")
2026-01-26T14:33:47.5215260Z 298 |         py_files = len(list(root.rglob("*.py")))
2026-01-26T14:33:47.5215320Z     |
2026-01-26T14:33:47.5215408Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5215413Z 
2026-01-26T14:33:47.5215500Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5215584Z    --> mcp_server.py:300:1
2026-01-26T14:33:47.5215644Z     |
2026-01-26T14:33:47.5215750Z 298 |         py_files = len(list(root.rglob("*.py")))
2026-01-26T14:33:47.5215937Z 299 |         js_files = len(list(root.rglob("*.js"))) + len(list(root.rglob("*.ts")))
2026-01-26T14:33:47.5215999Z 300 |         
2026-01-26T14:33:47.5216060Z     | ^^^^^^^^
2026-01-26T14:33:47.5216194Z 301 |         summary_parts.append("\n## Codebase Stats")
2026-01-26T14:33:47.5216335Z 302 |         summary_parts.append(f"- Python files: {py_files}")
2026-01-26T14:33:47.5216396Z     |
2026-01-26T14:33:47.5216489Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5216495Z 
2026-01-26T14:33:47.5216584Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5216661Z    --> mcp_server.py:304:1
2026-01-26T14:33:47.5216720Z     |
2026-01-26T14:33:47.5216858Z 302 |         summary_parts.append(f"- Python files: {py_files}")
2026-01-26T14:33:47.5217041Z 303 |         summary_parts.append(f"- JavaScript/TypeScript files: {js_files}")
2026-01-26T14:33:47.5217102Z 304 |         
2026-01-26T14:33:47.5217172Z     | ^^^^^^^^
2026-01-26T14:33:47.5217250Z 305 |         stats = get_index_stats()
2026-01-26T14:33:47.5217357Z 306 |         summary_parts.append(f"- {stats}")
2026-01-26T14:33:47.5217417Z     |
2026-01-26T14:33:47.5217509Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5217514Z 
2026-01-26T14:33:47.5217596Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5217673Z    --> mcp_server.py:307:1
2026-01-26T14:33:47.5217738Z     |
2026-01-26T14:33:47.5217816Z 305 |         stats = get_index_stats()
2026-01-26T14:33:47.5217909Z 306 |         summary_parts.append(f"- {stats}")
2026-01-26T14:33:47.5217971Z 307 |         
2026-01-26T14:33:47.5218039Z     | ^^^^^^^^
2026-01-26T14:33:47.5218132Z 308 |         return '\n'.join(summary_parts)
2026-01-26T14:33:47.5218211Z 309 |     except Exception as e:
2026-01-26T14:33:47.5218276Z     |
2026-01-26T14:33:47.5218365Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5218370Z 
2026-01-26T14:33:47.5218477Z C901 `extract_tech_stack` is too complex (19 > 10)
2026-01-26T14:33:47.5218557Z    --> mcp_server.py:314:5
2026-01-26T14:33:47.5218617Z     |
2026-01-26T14:33:47.5218688Z 313 | @mcp.tool()
2026-01-26T14:33:47.5218976Z 314 | def extract_tech_stack() -> str:
2026-01-26T14:33:47.5219108Z     |     ^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5219187Z 315 |     try:
2026-01-26T14:33:47.5219262Z 316 |         tech_stack = []
2026-01-26T14:33:47.5219328Z     |
2026-01-26T14:33:47.5219334Z 
2026-01-26T14:33:47.5219421Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5219501Z    --> mcp_server.py:317:1
2026-01-26T14:33:47.5219561Z     |
2026-01-26T14:33:47.5219628Z 315 |     try:
2026-01-26T14:33:47.5219700Z 316 |         tech_stack = []
2026-01-26T14:33:47.5219761Z 317 |         
2026-01-26T14:33:47.5219827Z     | ^^^^^^^^
2026-01-26T14:33:47.5219932Z 318 |         if Path("pyproject.toml").exists():
2026-01-26T14:33:47.5220202Z 319 |             content = Path("pyproject.toml").read_text()
2026-01-26T14:33:47.5220263Z     |
2026-01-26T14:33:47.5220361Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5220366Z 
2026-01-26T14:33:47.5220550Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5220633Z    --> mcp_server.py:334:1
2026-01-26T14:33:47.5220699Z     |
2026-01-26T14:33:47.5220786Z 332 |                         if '"' in line:
2026-01-26T14:33:47.5220914Z 333 |                             tech_stack.append(f"- {line.strip()}")
2026-01-26T14:33:47.5220982Z 334 |         
2026-01-26T14:33:47.5221044Z     | ^^^^^^^^
2026-01-26T14:33:47.5221156Z 335 |         elif Path("requirements.txt").exists():
2026-01-26T14:33:47.5221281Z 336 |             content = Path("requirements.txt").read_text()
2026-01-26T14:33:47.5221346Z     |
2026-01-26T14:33:47.5221435Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5221440Z 
2026-01-26T14:33:47.5221522Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5221607Z    --> mcp_server.py:342:1
2026-01-26T14:33:47.5221667Z     |
2026-01-26T14:33:47.5221797Z 340 |                 if line.strip() and not line.startswith('#'):
2026-01-26T14:33:47.5221921Z 341 |                     tech_stack.append(f"- {line.strip()}")
2026-01-26T14:33:47.5221982Z 342 |         
2026-01-26T14:33:47.5222043Z     | ^^^^^^^^
2026-01-26T14:33:47.5222140Z 343 |         if Path("package.json").exists():
2026-01-26T14:33:47.5222219Z 344 |             import json
2026-01-26T14:33:47.5222278Z     |
2026-01-26T14:33:47.5222364Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5222369Z 
2026-01-26T14:33:47.5222455Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5222529Z    --> mcp_server.py:354:1
2026-01-26T14:33:47.5222589Z     |
2026-01-26T14:33:47.5222694Z 352 |                 if len(data["dependencies"]) > 15:
2026-01-26T14:33:47.5222891Z 353 |                     tech_stack.append(f"... and {len(data['dependencies']) - 15} more")
2026-01-26T14:33:47.5222957Z 354 |         
2026-01-26T14:33:47.5223019Z     | ^^^^^^^^
2026-01-26T14:33:47.5223116Z 355 |         if Path("Cargo.toml").exists():
2026-01-26T14:33:47.5223226Z 356 |             tech_stack.append("\n## Rust Project")
2026-01-26T14:33:47.5223289Z     |
2026-01-26T14:33:47.5223380Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5223385Z 
2026-01-26T14:33:47.5223467Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5223544Z    --> mcp_server.py:357:1
2026-01-26T14:33:47.5223604Z     |
2026-01-26T14:33:47.5223697Z 355 |         if Path("Cargo.toml").exists():
2026-01-26T14:33:47.5223801Z 356 |             tech_stack.append("\n## Rust Project")
2026-01-26T14:33:47.5223864Z 357 |         
2026-01-26T14:33:47.5223930Z     | ^^^^^^^^
2026-01-26T14:33:47.5224013Z 358 |         if Path("go.mod").exists():
2026-01-26T14:33:47.5224117Z 359 |             tech_stack.append("\n## Go Project")
2026-01-26T14:33:47.5224185Z     |
2026-01-26T14:33:47.5224275Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5224280Z 
2026-01-26T14:33:47.5224360Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5224435Z    --> mcp_server.py:360:1
2026-01-26T14:33:47.5224500Z     |
2026-01-26T14:33:47.5224585Z 358 |         if Path("go.mod").exists():
2026-01-26T14:33:47.5224684Z 359 |             tech_stack.append("\n## Go Project")
2026-01-26T14:33:47.5224750Z 360 |         
2026-01-26T14:33:47.5224811Z     | ^^^^^^^^
2026-01-26T14:33:47.5224886Z 361 |         if not tech_stack:
2026-01-26T14:33:47.5225121Z 362 |             return "No standard dependency files found (pyproject.toml, package.json, etc.)"
2026-01-26T14:33:47.5225187Z     |
2026-01-26T14:33:47.5225273Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5225278Z 
2026-01-26T14:33:47.5225359Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5225439Z    --> mcp_server.py:363:1
2026-01-26T14:33:47.5225499Z     |
2026-01-26T14:33:47.5225574Z 361 |         if not tech_stack:
2026-01-26T14:33:47.5225886Z 362 |             return "No standard dependency files found (pyproject.toml, package.json, etc.)"
2026-01-26T14:33:47.5225949Z 363 |         
2026-01-26T14:33:47.5226011Z     | ^^^^^^^^
2026-01-26T14:33:47.5226169Z 364 |         return '\n'.join(tech_stack)
2026-01-26T14:33:47.5226254Z 365 |     except Exception as e:
2026-01-26T14:33:47.5226314Z     |
2026-01-26T14:33:47.5226399Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5226404Z 
2026-01-26T14:33:47.5226537Z C901 `analyze_project_structure` is too complex (13 > 10)
2026-01-26T14:33:47.5226612Z    --> mcp_server.py:370:5
2026-01-26T14:33:47.5226672Z     |
2026-01-26T14:33:47.5226744Z 369 | @mcp.tool()
2026-01-26T14:33:47.5226842Z 370 | def analyze_project_structure() -> str:
2026-01-26T14:33:47.5226914Z     |     ^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5226977Z 371 |     try:
2026-01-26T14:33:47.5227058Z 372 |         root = Path(".")
2026-01-26T14:33:47.5227118Z     |
2026-01-26T14:33:47.5227123Z 
2026-01-26T14:33:47.5227209Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5227289Z    --> mcp_server.py:374:1
2026-01-26T14:33:47.5227348Z     |
2026-01-26T14:33:47.5227428Z 372 |         root = Path(".")
2026-01-26T14:33:47.5227524Z 373 |         ignored_dirs = get_ignored_dirs()
2026-01-26T14:33:47.5227593Z 374 |         
2026-01-26T14:33:47.5227655Z     | ^^^^^^^^
2026-01-26T14:33:47.5227727Z 375 |         structure = []
2026-01-26T14:33:47.5227843Z 376 |         structure.append("# PROJECT STRUCTURE\n")
2026-01-26T14:33:47.5227903Z     |
2026-01-26T14:33:47.5227989Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5227994Z 
2026-01-26T14:33:47.5228080Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5228155Z    --> mcp_server.py:377:1
2026-01-26T14:33:47.5228214Z     |
2026-01-26T14:33:47.5228286Z 375 |         structure = []
2026-01-26T14:33:47.5228398Z 376 |         structure.append("# PROJECT STRUCTURE\n")
2026-01-26T14:33:47.5228460Z 377 |         
2026-01-26T14:33:47.5228525Z     | ^^^^^^^^
2026-01-26T14:33:47.5228603Z 378 |         dirs_by_depth = {}
2026-01-26T14:33:47.5228691Z 379 |         for item in root.iterdir():
2026-01-26T14:33:47.5228751Z     |
2026-01-26T14:33:47.5229053Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5229065Z 
2026-01-26T14:33:47.5229157Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5229233Z    --> mcp_server.py:382:1
2026-01-26T14:33:47.5229293Z     |
2026-01-26T14:33:47.5229438Z 380 |             if item.is_dir() and item.name not in ignored_dirs:
2026-01-26T14:33:47.5229581Z 381 |                 dirs_by_depth[item.name] = len(list(item.rglob("*")))
2026-01-26T14:33:47.5229644Z 382 |         
2026-01-26T14:33:47.5229710Z     | ^^^^^^^^
2026-01-26T14:33:47.5229931Z 383 |         sorted_dirs = sorted(dirs_by_depth.items(), key=lambda x: x[1], reverse=True)[:10]
2026-01-26T14:33:47.5230001Z     |
2026-01-26T14:33:47.5230091Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5230096Z 
2026-01-26T14:33:47.5230187Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5230262Z    --> mcp_server.py:384:1
2026-01-26T14:33:47.5230322Z     |
2026-01-26T14:33:47.5230533Z 383 |         sorted_dirs = sorted(dirs_by_depth.items(), key=lambda x: x[1], reverse=True)[:10]
2026-01-26T14:33:47.5230598Z 384 |         
2026-01-26T14:33:47.5230659Z     | ^^^^^^^^
2026-01-26T14:33:47.5230788Z 385 |         structure.append("## Main Directories (by size)")
2026-01-26T14:33:47.5230890Z 386 |         for dir_name, count in sorted_dirs:
2026-01-26T14:33:47.5230951Z     |
2026-01-26T14:33:47.5231036Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5231040Z 
2026-01-26T14:33:47.5231127Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5231200Z    --> mcp_server.py:388:1
2026-01-26T14:33:47.5231261Z     |
2026-01-26T14:33:47.5231358Z 386 |         for dir_name, count in sorted_dirs:
2026-01-26T14:33:47.5231494Z 387 |             structure.append(f"- `{dir_name}/` ({count} items)")
2026-01-26T14:33:47.5231568Z 388 |         
2026-01-26T14:33:47.5231763Z     | ^^^^^^^^
2026-01-26T14:33:47.5231843Z 389 |         file_types = {}
2026-01-26T14:33:47.5232026Z 390 |         for ext in ['.py', '.js', '.ts', '.jsx', '.tsx', '.go', '.rs', '.java', '.c', '.cpp']:
2026-01-26T14:33:47.5232187Z     |
2026-01-26T14:33:47.5232287Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5232292Z 
2026-01-26T14:33:47.5232375Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5232455Z    --> mcp_server.py:394:1
2026-01-26T14:33:47.5232520Z     |
2026-01-26T14:33:47.5232619Z 392 |             if count > 0:
2026-01-26T14:33:47.5232714Z 393 |                 file_types[ext] = count
2026-01-26T14:33:47.5232776Z 394 |         
2026-01-26T14:33:47.5232923Z     | ^^^^^^^^
2026-01-26T14:33:47.5233053Z 395 |         if file_types:
2026-01-26T14:33:47.5233186Z 396 |             structure.append("\n## File Types")
2026-01-26T14:33:47.5233252Z     |
2026-01-26T14:33:47.5233341Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5233352Z 
2026-01-26T14:33:47.5233436Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5233520Z    --> mcp_server.py:399:1
2026-01-26T14:33:47.5233580Z     |
2026-01-26T14:33:47.5233797Z 397 |             for ext, count in sorted(file_types.items(), key=lambda x: x[1], reverse=True):
2026-01-26T14:33:47.5233923Z 398 |                 structure.append(f"- `{ext}`: {count} files")
2026-01-26T14:33:47.5233990Z 399 |         
2026-01-26T14:33:47.5234051Z     | ^^^^^^^^
2026-01-26T14:33:47.5234125Z 400 |         config_files = []
2026-01-26T14:33:47.5234306Z 401 |         for cfg in ['pyproject.toml', 'package.json', 'Cargo.toml', 'go.mod', 
2026-01-26T14:33:47.5234366Z     |
2026-01-26T14:33:47.5234452Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5234457Z 
2026-01-26T14:33:47.5234537Z W291 [*] Trailing whitespace
2026-01-26T14:33:47.5234616Z    --> mcp_server.py:401:78
2026-01-26T14:33:47.5234677Z     |
2026-01-26T14:33:47.5234759Z 400 |         config_files = []
2026-01-26T14:33:47.5234940Z 401 |         for cfg in ['pyproject.toml', 'package.json', 'Cargo.toml', 'go.mod', 
2026-01-26T14:33:47.5235053Z     |                                                                              ^
2026-01-26T14:33:47.5235240Z 402 |                     '.gitignore', 'docker-compose.yml', 'Dockerfile', '.env.example']:
2026-01-26T14:33:47.5235330Z 403 |             if Path(cfg).exists():
2026-01-26T14:33:47.5235390Z     |
2026-01-26T14:33:47.5235475Z help: Remove trailing whitespace
2026-01-26T14:33:47.5235482Z 
2026-01-26T14:33:47.5235573Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5235650Z    --> mcp_server.py:405:1
2026-01-26T14:33:47.5235709Z     |
2026-01-26T14:33:47.5235790Z 403 |             if Path(cfg).exists():
2026-01-26T14:33:47.5235886Z 404 |                 config_files.append(cfg)
2026-01-26T14:33:47.5235949Z 405 |         
2026-01-26T14:33:47.5236010Z     | ^^^^^^^^
2026-01-26T14:33:47.5236088Z 406 |         if config_files:
2026-01-26T14:33:47.5236214Z 407 |             structure.append("\n## Configuration Files")
2026-01-26T14:33:47.5236292Z     |
2026-01-26T14:33:47.5236380Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5236386Z 
2026-01-26T14:33:47.5236474Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5236554Z    --> mcp_server.py:410:1
2026-01-26T14:33:47.5236614Z     |
2026-01-26T14:33:47.5236703Z 408 |             for cfg in config_files:
2026-01-26T14:33:47.5236799Z 409 |                 structure.append(f"- {cfg}")
2026-01-26T14:33:47.5236859Z 410 |         
2026-01-26T14:33:47.5236928Z     | ^^^^^^^^
2026-01-26T14:33:47.5237030Z 411 |         return '\n'.join(structure)
2026-01-26T14:33:47.5237109Z 412 |     except Exception as e:
2026-01-26T14:33:47.5237168Z     |
2026-01-26T14:33:47.5237261Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5237266Z 
2026-01-26T14:33:47.5237395Z C901 `get_recent_changes_summary` is too complex (12 > 10)
2026-01-26T14:33:47.5237471Z    --> mcp_server.py:417:5
2026-01-26T14:33:47.5237630Z     |
2026-01-26T14:33:47.5237698Z 416 | @mcp.tool()
2026-01-26T14:33:47.5237830Z 417 | def get_recent_changes_summary(days: int = 7) -> str:
2026-01-26T14:33:47.5237901Z     |     ^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5238107Z 418 |     if days <= 0 or days > 365:
2026-01-26T14:33:47.5238228Z 419 |         return "Error: days must be between 1 and 365"
2026-01-26T14:33:47.5238289Z     |
2026-01-26T14:33:47.5238294Z 
2026-01-26T14:33:47.5238383Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5238459Z    --> mcp_server.py:420:1
2026-01-26T14:33:47.5238519Z     |
2026-01-26T14:33:47.5238606Z 418 |     if days <= 0 or days > 365:
2026-01-26T14:33:47.5238722Z 419 |         return "Error: days must be between 1 and 365"
2026-01-26T14:33:47.5239086Z 420 |     
2026-01-26T14:33:47.5239200Z     | ^^^^
2026-01-26T14:33:47.5239274Z 421 |     try:
2026-01-26T14:33:47.5239440Z 422 |         repo = git.Repo(os.getcwd(), search_parent_directories=True)
2026-01-26T14:33:47.5239502Z     |
2026-01-26T14:33:47.5239601Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5239607Z 
2026-01-26T14:33:47.5239693Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5239771Z    --> mcp_server.py:427:1
2026-01-26T14:33:47.5239831Z     |
2026-01-26T14:33:47.5239918Z 425 |     except Exception as e:
2026-01-26T14:33:47.5240015Z 426 |         return f"Error accessing git: {e}"
2026-01-26T14:33:47.5240076Z 427 |     
2026-01-26T14:33:47.5240141Z     | ^^^^
2026-01-26T14:33:47.5240205Z 428 |     try:
2026-01-26T14:33:47.5240297Z 429 |         from datetime import timedelta
2026-01-26T14:33:47.5240358Z     |
2026-01-26T14:33:47.5240450Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5240455Z 
2026-01-26T14:33:47.5240537Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5240612Z    --> mcp_server.py:431:1
2026-01-26T14:33:47.5240677Z     |
2026-01-26T14:33:47.5240768Z 429 |         from datetime import timedelta
2026-01-26T14:33:47.5240923Z 430 |         cutoff_date = datetime.now() - timedelta(days=days)
2026-01-26T14:33:47.5240994Z 431 |         
2026-01-26T14:33:47.5241056Z     | ^^^^^^^^
2026-01-26T14:33:47.5241125Z 432 |         commits = []
2026-01-26T14:33:47.5241248Z 433 |         for commit in repo.iter_commits(max_count=100):
2026-01-26T14:33:47.5241317Z     |
2026-01-26T14:33:47.5241402Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5241407Z 
2026-01-26T14:33:47.5241487Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5241567Z    --> mcp_server.py:438:1
2026-01-26T14:33:47.5241627Z     |
2026-01-26T14:33:47.5241695Z 436 |                 break
2026-01-26T14:33:47.5241786Z 437 |             commits.append(commit)
2026-01-26T14:33:47.5241848Z 438 |         
2026-01-26T14:33:47.5241910Z     | ^^^^^^^^
2026-01-26T14:33:47.5241983Z 439 |         if not commits:
2026-01-26T14:33:47.5242121Z 440 |             return f"No commits found in the last {days} days"
2026-01-26T14:33:47.5242180Z     |
2026-01-26T14:33:47.5242267Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5242274Z 
2026-01-26T14:33:47.5242362Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5242437Z    --> mcp_server.py:441:1
2026-01-26T14:33:47.5242500Z     |
2026-01-26T14:33:47.5242571Z 439 |         if not commits:
2026-01-26T14:33:47.5242704Z 440 |             return f"No commits found in the last {days} days"
2026-01-26T14:33:47.5242768Z 441 |         
2026-01-26T14:33:47.5242828Z     | ^^^^^^^^
2026-01-26T14:33:47.5242951Z 442 |         summary = [f"# CHANGES IN LAST {days} DAYS\n"]
2026-01-26T14:33:47.5243083Z 443 |         summary.append(f"Total commits: {len(commits)}\n")
2026-01-26T14:33:47.5243142Z     |
2026-01-26T14:33:47.5243235Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5243241Z 
2026-01-26T14:33:47.5243324Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5243409Z    --> mcp_server.py:444:1
2026-01-26T14:33:47.5243482Z     |
2026-01-26T14:33:47.5243601Z 442 |         summary = [f"# CHANGES IN LAST {days} DAYS\n"]
2026-01-26T14:33:47.5243875Z 443 |         summary.append(f"Total commits: {len(commits)}\n")
2026-01-26T14:33:47.5243937Z 444 |         
2026-01-26T14:33:47.5244003Z     | ^^^^^^^^
2026-01-26T14:33:47.5244073Z 445 |         authors = {}
2026-01-26T14:33:47.5244249Z 446 |         for commit in commits:
2026-01-26T14:33:47.5244311Z     |
2026-01-26T14:33:47.5244404Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5244408Z 
2026-01-26T14:33:47.5244489Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5244565Z    --> mcp_server.py:449:1
2026-01-26T14:33:47.5244630Z     |
2026-01-26T14:33:47.5244723Z 447 |             author = commit.author.name
2026-01-26T14:33:47.5244849Z 448 |             authors[author] = authors.get(author, 0) + 1
2026-01-26T14:33:47.5244915Z 449 |         
2026-01-26T14:33:47.5244983Z     | ^^^^^^^^
2026-01-26T14:33:47.5245096Z 450 |         summary.append("## Contributors")
2026-01-26T14:33:47.5245314Z 451 |         for author, count in sorted(authors.items(), key=lambda x: x[1], reverse=True):
2026-01-26T14:33:47.5245385Z     |
2026-01-26T14:33:47.5245473Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5245478Z 
2026-01-26T14:33:47.5245592Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5245673Z    --> mcp_server.py:453:1
2026-01-26T14:33:47.5245736Z     |
2026-01-26T14:33:47.5245940Z 451 |         for author, count in sorted(authors.items(), key=lambda x: x[1], reverse=True):
2026-01-26T14:33:47.5246071Z 452 |             summary.append(f"- {author}: {count} commits")
2026-01-26T14:33:47.5246132Z 453 |         
2026-01-26T14:33:47.5246192Z     | ^^^^^^^^
2026-01-26T14:33:47.5246292Z 454 |         summary.append("\n## Recent Commits")
2026-01-26T14:33:47.5246386Z 455 |         for commit in commits[:10]:
2026-01-26T14:33:47.5246447Z     |
2026-01-26T14:33:47.5246534Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5246538Z 
2026-01-26T14:33:47.5246626Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5246705Z    --> mcp_server.py:459:1
2026-01-26T14:33:47.5246768Z     |
2026-01-26T14:33:47.5246933Z 457 |             message = commit.message.strip().split('\n')[0][:100]
2026-01-26T14:33:47.5247109Z 458 |             summary.append(f"- **{date_str}** [{commit.hexsha[:7]}]: {message}")
2026-01-26T14:33:47.5247174Z 459 |         
2026-01-26T14:33:47.5247235Z     | ^^^^^^^^
2026-01-26T14:33:47.5247322Z 460 |         if len(commits) > 10:
2026-01-26T14:33:47.5247493Z 461 |             summary.append(f"\n... and {len(commits) - 10} more commits")
2026-01-26T14:33:47.5247554Z     |
2026-01-26T14:33:47.5247647Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5247652Z 
2026-01-26T14:33:47.5247733Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5247809Z    --> mcp_server.py:462:1
2026-01-26T14:33:47.5247869Z     |
2026-01-26T14:33:47.5247949Z 460 |         if len(commits) > 10:
2026-01-26T14:33:47.5248102Z 461 |             summary.append(f"\n... and {len(commits) - 10} more commits")
2026-01-26T14:33:47.5248165Z 462 |         
2026-01-26T14:33:47.5248235Z     | ^^^^^^^^
2026-01-26T14:33:47.5248312Z 463 |         return '\n'.join(summary)
2026-01-26T14:33:47.5248391Z 464 |     except Exception as e:
2026-01-26T14:33:47.5248456Z     |
2026-01-26T14:33:47.5248544Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5248549Z 
2026-01-26T14:33:47.5248631Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5248708Z    --> mcp_server.py:472:1
2026-01-26T14:33:47.5248935Z     |
2026-01-26T14:33:47.5249094Z 470 |     if vector_store.get_collection() is None:
2026-01-26T14:33:47.5249213Z 471 |         return "Failed to initialize vector store."
2026-01-26T14:33:47.5249280Z 472 |     
2026-01-26T14:33:47.5249341Z     | ^^^^
2026-01-26T14:33:47.5249419Z 473 |     root_dir = Path(".")
2026-01-26T14:33:47.5249510Z 474 |     ignored_dirs = get_ignored_dirs()
2026-01-26T14:33:47.5249576Z     |
2026-01-26T14:33:47.5249662Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5249667Z 
2026-01-26T14:33:47.5249747Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5249962Z    --> mcp_server.py:476:1
2026-01-26T14:33:47.5250023Z     |
2026-01-26T14:33:47.5250110Z 474 |     ignored_dirs = get_ignored_dirs()
2026-01-26T14:33:47.5250339Z 475 |     ignore_patterns = load_index_ignore_patterns()
2026-01-26T14:33:47.5250404Z 476 |     
2026-01-26T14:33:47.5250464Z     | ^^^^
2026-01-26T14:33:47.5250645Z 477 |     return indexer.index_changed(root_dir, ignored_dirs, ignore_patterns)
2026-01-26T14:33:47.5250709Z     |
2026-01-26T14:33:47.5250795Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5250800Z 
2026-01-26T14:33:47.5250897Z UP045 [*] Use `X | None` for type annotations
2026-01-26T14:33:47.5250980Z    --> mcp_server.py:483:17
2026-01-26T14:33:47.5251040Z     |
2026-01-26T14:33:47.5251109Z 481 |     source: str,
2026-01-26T14:33:47.5251189Z 482 |     relevance: float,
2026-01-26T14:33:47.5251279Z 483 |     file_types: Optional[List[str]],
2026-01-26T14:33:47.5251352Z     |                 ^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5251447Z 484 |     exclude_dirs: Optional[List[str]],
2026-01-26T14:33:47.5251529Z 485 |     min_relevance: float
2026-01-26T14:33:47.5251588Z     |
2026-01-26T14:33:47.5251663Z help: Convert to `X | None`
2026-01-26T14:33:47.5251668Z 
2026-01-26T14:33:47.5251799Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5251875Z    --> mcp_server.py:483:26
2026-01-26T14:33:47.5251934Z     |
2026-01-26T14:33:47.5252001Z 481 |     source: str,
2026-01-26T14:33:47.5252078Z 482 |     relevance: float,
2026-01-26T14:33:47.5252167Z 483 |     file_types: Optional[List[str]],
2026-01-26T14:33:47.5252237Z     |                          ^^^^
2026-01-26T14:33:47.5252332Z 484 |     exclude_dirs: Optional[List[str]],
2026-01-26T14:33:47.5252408Z 485 |     min_relevance: float
2026-01-26T14:33:47.5252469Z     |
2026-01-26T14:33:47.5252547Z help: Replace with `list`
2026-01-26T14:33:47.5252557Z 
2026-01-26T14:33:47.5252649Z UP045 [*] Use `X | None` for type annotations
2026-01-26T14:33:47.5252729Z    --> mcp_server.py:484:19
2026-01-26T14:33:47.5252790Z     |
2026-01-26T14:33:47.5252866Z 482 |     relevance: float,
2026-01-26T14:33:47.5252952Z 483 |     file_types: Optional[List[str]],
2026-01-26T14:33:47.5253044Z 484 |     exclude_dirs: Optional[List[str]],
2026-01-26T14:33:47.5253122Z     |                   ^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5253197Z 485 |     min_relevance: float
2026-01-26T14:33:47.5253263Z 486 | ) -> bool:
2026-01-26T14:33:47.5253323Z     |
2026-01-26T14:33:47.5253403Z help: Convert to `X | None`
2026-01-26T14:33:47.5253407Z 
2026-01-26T14:33:47.5253526Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5253600Z    --> mcp_server.py:484:28
2026-01-26T14:33:47.5253667Z     |
2026-01-26T14:33:47.5253738Z 482 |     relevance: float,
2026-01-26T14:33:47.5253828Z 483 |     file_types: Optional[List[str]],
2026-01-26T14:33:47.5253923Z 484 |     exclude_dirs: Optional[List[str]],
2026-01-26T14:33:47.5253995Z     |                            ^^^^
2026-01-26T14:33:47.5254072Z 485 |     min_relevance: float
2026-01-26T14:33:47.5254136Z 486 | ) -> bool:
2026-01-26T14:33:47.5254202Z     |
2026-01-26T14:33:47.5254281Z help: Replace with `list`
2026-01-26T14:33:47.5254285Z 
2026-01-26T14:33:47.5254369Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5254450Z    --> mcp_server.py:489:1
2026-01-26T14:33:47.5254512Z     |
2026-01-26T14:33:47.5254574Z 487 |     """
2026-01-26T14:33:47.5254747Z 488 |     Determines if a search result should be included based on filters.
2026-01-26T14:33:47.5254814Z 489 |     
2026-01-26T14:33:47.5254876Z     | ^^^^
2026-01-26T14:33:47.5254939Z 490 |     Args:
2026-01-26T14:33:47.5255034Z 491 |         source: File path of the result
2026-01-26T14:33:47.5255095Z     |
2026-01-26T14:33:47.5255184Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5255189Z 
2026-01-26T14:33:47.5255275Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5255351Z    --> mcp_server.py:496:1
2026-01-26T14:33:47.5255411Z     |
2026-01-26T14:33:47.5255627Z 494 |         exclude_dirs: Directories to exclude (None = none)
2026-01-26T14:33:47.5255745Z 495 |         min_relevance: Minimum relevance threshold
2026-01-26T14:33:47.5255807Z 496 |         
2026-01-26T14:33:47.5255869Z     | ^^^^^^^^
2026-01-26T14:33:47.5256009Z 497 |     Returns:
2026-01-26T14:33:47.5256108Z 498 |         True if result passes all filters
2026-01-26T14:33:47.5256168Z     |
2026-01-26T14:33:47.5256254Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5256259Z 
2026-01-26T14:33:47.5256345Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5256419Z    --> mcp_server.py:502:1
2026-01-26T14:33:47.5256479Z     |
2026-01-26T14:33:47.5256612Z 500 |     if min_relevance > 0 and relevance < min_relevance:
2026-01-26T14:33:47.5256681Z 501 |         return False
2026-01-26T14:33:47.5256741Z 502 |     
2026-01-26T14:33:47.5256803Z     | ^^^^
2026-01-26T14:33:47.5256879Z 503 |     if file_types:
2026-01-26T14:33:47.5256968Z 504 |         file_ext = Path(source).suffix
2026-01-26T14:33:47.5257032Z     |
2026-01-26T14:33:47.5257121Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5257126Z 
2026-01-26T14:33:47.5257208Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5257286Z    --> mcp_server.py:507:1
2026-01-26T14:33:47.5257349Z     |
2026-01-26T14:33:47.5257435Z 505 |         if file_ext not in file_types:
2026-01-26T14:33:47.5257504Z 506 |             return False
2026-01-26T14:33:47.5257564Z 507 |     
2026-01-26T14:33:47.5257630Z     | ^^^^
2026-01-26T14:33:47.5257699Z 508 |     if exclude_dirs:
2026-01-26T14:33:47.5257783Z 509 |         for exc_dir in exclude_dirs:
2026-01-26T14:33:47.5257848Z     |
2026-01-26T14:33:47.5257933Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5257938Z 
2026-01-26T14:33:47.5258020Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5258094Z    --> mcp_server.py:512:1
2026-01-26T14:33:47.5258159Z     |
2026-01-26T14:33:47.5258235Z 510 |             if exc_dir in source:
2026-01-26T14:33:47.5258311Z 511 |                 return False
2026-01-26T14:33:47.5258377Z 512 |     
2026-01-26T14:33:47.5258438Z     | ^^^^
2026-01-26T14:33:47.5258506Z 513 |     return True
2026-01-26T14:33:47.5258565Z     |
2026-01-26T14:33:47.5258660Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5258665Z 
2026-01-26T14:33:47.5258745Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5258930Z    --> mcp_server.py:519:1
2026-01-26T14:33:47.5258997Z     |
2026-01-26T14:33:47.5259058Z 517 |     """
2026-01-26T14:33:47.5259170Z 518 |     Formats a single search result for display.
2026-01-26T14:33:47.5259237Z 519 |     
2026-01-26T14:33:47.5259297Z     | ^^^^
2026-01-26T14:33:47.5259360Z 520 |     Args:
2026-01-26T14:33:47.5259442Z 521 |         source: Source file path
2026-01-26T14:33:47.5259507Z     |
2026-01-26T14:33:47.5259593Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5259597Z 
2026-01-26T14:33:47.5259677Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5259762Z    --> mcp_server.py:524:1
2026-01-26T14:33:47.5259821Z     |
2026-01-26T14:33:47.5259905Z 522 |         document: Document content
2026-01-26T14:33:47.5259988Z 523 |         relevance: Relevance score
2026-01-26T14:33:47.5260055Z 524 |         
2026-01-26T14:33:47.5260119Z     | ^^^^^^^^
2026-01-26T14:33:47.5260183Z 525 |     Returns:
2026-01-26T14:33:47.5260268Z 526 |         Formatted result string
2026-01-26T14:33:47.5260330Z     |
2026-01-26T14:33:47.5260416Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5260421Z 
2026-01-26T14:33:47.5260550Z C901 `search_codebase_advanced` is too complex (11 > 10)
2026-01-26T14:33:47.5260627Z    --> mcp_server.py:532:5
2026-01-26T14:33:47.5260688Z     |
2026-01-26T14:33:47.5260754Z 531 | @mcp.tool()
2026-01-26T14:33:47.5260838Z 532 | def search_codebase_advanced(
2026-01-26T14:33:47.5260908Z     |     ^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5260975Z 533 |     query: str,
2026-01-26T14:33:47.5261055Z 534 |     n_results: int = 5,
2026-01-26T14:33:47.5261235Z     |
2026-01-26T14:33:47.5261239Z 
2026-01-26T14:33:47.5261334Z UP045 [*] Use `X | None` for type annotations
2026-01-26T14:33:47.5261411Z    --> mcp_server.py:535:17
2026-01-26T14:33:47.5261476Z     |
2026-01-26T14:33:47.5261542Z 533 |     query: str,
2026-01-26T14:33:47.5261713Z 534 |     n_results: int = 5,
2026-01-26T14:33:47.5261822Z 535 |     file_types: Optional[List[str]] = None,
2026-01-26T14:33:47.5261893Z     |                 ^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5261996Z 536 |     exclude_dirs: Optional[List[str]] = None,
2026-01-26T14:33:47.5262081Z 537 |     min_relevance: float = 0.0,
2026-01-26T14:33:47.5262141Z     |
2026-01-26T14:33:47.5262216Z help: Convert to `X | None`
2026-01-26T14:33:47.5262220Z 
2026-01-26T14:33:47.5262342Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5262424Z    --> mcp_server.py:535:26
2026-01-26T14:33:47.5262485Z     |
2026-01-26T14:33:47.5262552Z 533 |     query: str,
2026-01-26T14:33:47.5262629Z 534 |     n_results: int = 5,
2026-01-26T14:33:47.5262729Z 535 |     file_types: Optional[List[str]] = None,
2026-01-26T14:33:47.5262797Z     |                          ^^^^
2026-01-26T14:33:47.5262897Z 536 |     exclude_dirs: Optional[List[str]] = None,
2026-01-26T14:33:47.5262985Z 537 |     min_relevance: float = 0.0,
2026-01-26T14:33:47.5263045Z     |
2026-01-26T14:33:47.5263121Z help: Replace with `list`
2026-01-26T14:33:47.5263125Z 
2026-01-26T14:33:47.5263223Z UP045 [*] Use `X | None` for type annotations
2026-01-26T14:33:47.5263297Z    --> mcp_server.py:536:19
2026-01-26T14:33:47.5263358Z     |
2026-01-26T14:33:47.5263434Z 534 |     n_results: int = 5,
2026-01-26T14:33:47.5263527Z 535 |     file_types: Optional[List[str]] = None,
2026-01-26T14:33:47.5263623Z 536 |     exclude_dirs: Optional[List[str]] = None,
2026-01-26T14:33:47.5263698Z     |                   ^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5263784Z 537 |     min_relevance: float = 0.0,
2026-01-26T14:33:47.5263849Z 538 | ) -> str:
2026-01-26T14:33:47.5263909Z     |
2026-01-26T14:33:47.5263993Z help: Convert to `X | None`
2026-01-26T14:33:47.5263997Z 
2026-01-26T14:33:47.5264118Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5264192Z    --> mcp_server.py:536:28
2026-01-26T14:33:47.5264256Z     |
2026-01-26T14:33:47.5264331Z 534 |     n_results: int = 5,
2026-01-26T14:33:47.5264426Z 535 |     file_types: Optional[List[str]] = None,
2026-01-26T14:33:47.5264525Z 536 |     exclude_dirs: Optional[List[str]] = None,
2026-01-26T14:33:47.5264601Z     |                            ^^^^
2026-01-26T14:33:47.5264680Z 537 |     min_relevance: float = 0.0,
2026-01-26T14:33:47.5264744Z 538 | ) -> str:
2026-01-26T14:33:47.5264809Z     |
2026-01-26T14:33:47.5264885Z help: Replace with `list`
2026-01-26T14:33:47.5264890Z 
2026-01-26T14:33:47.5264973Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5265050Z    --> mcp_server.py:553:1
2026-01-26T14:33:47.5265114Z     |
2026-01-26T14:33:47.5265176Z 551 |     try:
2026-01-26T14:33:47.5265372Z 552 |         results = vector_store.query(query_texts=[query], n_results=n_results * 2)
2026-01-26T14:33:47.5265443Z 553 |         
2026-01-26T14:33:47.5265503Z     | ^^^^^^^^
2026-01-26T14:33:47.5265578Z 554 |         if results is None:
2026-01-26T14:33:47.5265689Z 555 |             return "Vector store not initialized."
2026-01-26T14:33:47.5265755Z     |
2026-01-26T14:33:47.5265841Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5265846Z 
2026-01-26T14:33:47.5265929Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5266011Z    --> mcp_server.py:569:1
2026-01-26T14:33:47.5266070Z     |
2026-01-26T14:33:47.5266341Z 567 |                 if should_include_search_result(source, relevance, file_types, exclude_dirs, min_relevance):
2026-01-26T14:33:47.5266516Z 568 |                     output.append(format_search_result(source, doc, relevance))
2026-01-26T14:33:47.5266582Z 569 |                 
2026-01-26T14:33:47.5266646Z     | ^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5266744Z 570 |                 if len(output) >= n_results:
2026-01-26T14:33:47.5266901Z 571 |                     break
2026-01-26T14:33:47.5266963Z     |
2026-01-26T14:33:47.5267049Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5267055Z 
2026-01-26T14:33:47.5267274Z C901 `auto_update_memory_from_commits` is too complex (12 > 10)
2026-01-26T14:33:47.5267355Z    --> mcp_server.py:580:5
2026-01-26T14:33:47.5267417Z     |
2026-01-26T14:33:47.5267488Z 579 | @mcp.tool()
2026-01-26T14:33:47.5267712Z 580 | def auto_update_memory_from_commits(days: int = 7, auto_summarize: bool = True) -> str:
2026-01-26T14:33:47.5267785Z     |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5267900Z 581 |     if days <= 0 or days > 90:
2026-01-26T14:33:47.5268023Z 582 |         return "Error: days must be between 1 and 90"
2026-01-26T14:33:47.5268083Z     |
2026-01-26T14:33:47.5268088Z 
2026-01-26T14:33:47.5268215Z C901 `analyze_code_complexity` is too complex (13 > 10)
2026-01-26T14:33:47.5268296Z    --> mcp_server.py:635:5
2026-01-26T14:33:47.5268360Z     |
2026-01-26T14:33:47.5268425Z 634 | @mcp.tool()
2026-01-26T14:33:47.5268575Z 635 | def analyze_code_complexity(target_path: str = ".") -> str:
2026-01-26T14:33:47.5268645Z     |     ^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5268710Z 636 |     try:
2026-01-26T14:33:47.5268908Z 637 |         from radon.complexity import cc_visit
2026-01-26T14:33:47.5268975Z     |
2026-01-26T14:33:47.5268980Z 
2026-01-26T14:33:47.5269314Z F401 `radon.metrics.mi_visit` imported but unused; consider using `importlib.util.find_spec` to test for availability
2026-01-26T14:33:47.5269393Z    --> mcp_server.py:638:35
2026-01-26T14:33:47.5269458Z     |
2026-01-26T14:33:47.5269520Z 636 |     try:
2026-01-26T14:33:47.5269619Z 637 |         from radon.complexity import cc_visit
2026-01-26T14:33:47.5269720Z 638 |         from radon.metrics import mi_visit
2026-01-26T14:33:47.5269800Z     |                                   ^^^^^^^^
2026-01-26T14:33:47.5269877Z 639 |     except ImportError:
2026-01-26T14:33:47.5270035Z 640 |         return "Error: radon not installed. Run: pip install radon"
2026-01-26T14:33:47.5270101Z     |
2026-01-26T14:33:47.5270217Z help: Remove unused import: `radon.metrics.mi_visit`
2026-01-26T14:33:47.5270222Z 
2026-01-26T14:33:47.5270308Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5270389Z    --> mcp_server.py:641:1
2026-01-26T14:33:47.5270453Z     |
2026-01-26T14:33:47.5270528Z 639 |     except ImportError:
2026-01-26T14:33:47.5270684Z 640 |         return "Error: radon not installed. Run: pip install radon"
2026-01-26T14:33:47.5270746Z 641 |     
2026-01-26T14:33:47.5270806Z     | ^^^^
2026-01-26T14:33:47.5270868Z 642 |     try:
2026-01-26T14:33:47.5270970Z 643 |         target = validate_path(target_path)
2026-01-26T14:33:47.5271029Z     |
2026-01-26T14:33:47.5271117Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5271121Z 
2026-01-26T14:33:47.5271219Z F541 [*] f-string without any placeholders
2026-01-26T14:33:47.5271295Z    --> mcp_server.py:683:24
2026-01-26T14:33:47.5271358Z     |
2026-01-26T14:33:47.5271540Z 682 |         avg_complexity = total_complexity / file_count if file_count > 0 else 0
2026-01-26T14:33:47.5271638Z 683 |         results.append(f"\n## Summary")
2026-01-26T14:33:47.5271717Z     |                        ^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5271849Z 684 |         results.append(f"- Files analyzed: {file_count}")
2026-01-26T14:33:47.5272044Z 685 |         results.append(f"- High complexity functions: {len(high_complexity)}")
2026-01-26T14:33:47.5272104Z     |
2026-01-26T14:33:47.5272191Z help: Remove extraneous `f` prefix
2026-01-26T14:33:47.5272196Z 
2026-01-26T14:33:47.5272318Z C901 `analyze_code_quality` is too complex (15 > 10)
2026-01-26T14:33:47.5272396Z    --> mcp_server.py:696:5
2026-01-26T14:33:47.5272455Z     |
2026-01-26T14:33:47.5272521Z 695 | @mcp.tool()
2026-01-26T14:33:47.5272719Z 696 | def analyze_code_quality(target_path: str = ".", max_files: int = 10) -> str:
2026-01-26T14:33:47.5272789Z     |     ^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5272977Z 697 |     try:
2026-01-26T14:33:47.5273073Z 698 |         from pylint.lint import Run
2026-01-26T14:33:47.5273133Z     |
2026-01-26T14:33:47.5273138Z 
2026-01-26T14:33:47.5273242Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5273422Z    --> mcp_server.py:698:9
2026-01-26T14:33:47.5273485Z     |
2026-01-26T14:33:47.5273677Z 696 |   def analyze_code_quality(target_path: str = ".", max_files: int = 10) -> str:
2026-01-26T14:33:47.5273741Z 697 |       try:
2026-01-26T14:33:47.5273836Z 698 | /         from pylint.lint import Run
2026-01-26T14:33:47.5273917Z 699 | |         from io import StringIO
2026-01-26T14:33:47.5273988Z     | |_______________________________^
2026-01-26T14:33:47.5274073Z 700 |       except ImportError:
2026-01-26T14:33:47.5274235Z 701 |           return "Error: pylint not installed. Run: pip install pylint"
2026-01-26T14:33:47.5274296Z     |
2026-01-26T14:33:47.5274374Z help: Organize imports
2026-01-26T14:33:47.5274379Z 
2026-01-26T14:33:47.5274466Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5274543Z    --> mcp_server.py:702:1
2026-01-26T14:33:47.5274602Z     |
2026-01-26T14:33:47.5274688Z 700 |     except ImportError:
2026-01-26T14:33:47.5274845Z 701 |         return "Error: pylint not installed. Run: pip install pylint"
2026-01-26T14:33:47.5274907Z 702 |     
2026-01-26T14:33:47.5274972Z     | ^^^^
2026-01-26T14:33:47.5275038Z 703 |     try:
2026-01-26T14:33:47.5275138Z 704 |         target = validate_path(target_path)
2026-01-26T14:33:47.5275198Z     |
2026-01-26T14:33:47.5275289Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5275294Z 
2026-01-26T14:33:47.5275380Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5275454Z    --> mcp_server.py:823:1
2026-01-26T14:33:47.5275520Z     |
2026-01-26T14:33:47.5275580Z 821 |     """
2026-01-26T14:33:47.5275700Z 822 |     Returns performance statistics for all caches.
2026-01-26T14:33:47.5275765Z 823 |     
2026-01-26T14:33:47.5275825Z     | ^^^^
2026-01-26T14:33:47.5275893Z 824 |     Returns:
2026-01-26T14:33:47.5275996Z 825 |         Formatted string with cache statistics
2026-01-26T14:33:47.5276062Z     |
2026-01-26T14:33:47.5276147Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5276152Z 
2026-01-26T14:33:47.5276236Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5276317Z    --> mcp_server.py:829:1
2026-01-26T14:33:47.5276377Z     |
2026-01-26T14:33:47.5276471Z 827 |     file_stats = get_file_cache_stats()
2026-01-26T14:33:47.5276600Z 828 |     query_stats = vector_store.get_query_cache_stats()
2026-01-26T14:33:47.5276667Z 829 |     
2026-01-26T14:33:47.5276729Z     | ^^^^
2026-01-26T14:33:47.5276814Z 830 |     result = "# CACHE STATISTICS\n\n"
2026-01-26T14:33:47.5276927Z 831 |     result += "## File Cache (safe_read_text)\n"
2026-01-26T14:33:47.5276988Z     |
2026-01-26T14:33:47.5277075Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5277080Z 
2026-01-26T14:33:47.5277167Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5277244Z    --> mcp_server.py:836:1
2026-01-26T14:33:47.5277303Z     |
2026-01-26T14:33:47.5277443Z 834 |     result += f"- **Hit Rate**: {file_stats['hit_rate']}\n"
2026-01-26T14:33:47.5277624Z 835 |     result += f"- **Size**: {file_stats['size']}/{file_stats['capacity']}\n\n"
2026-01-26T14:33:47.5277686Z 836 |     
2026-01-26T14:33:47.5277745Z     | ^^^^
2026-01-26T14:33:47.5277857Z 837 |     result += "## Query Cache (vector search)\n"
2026-01-26T14:33:47.5277968Z 838 |     result += f"- **Hits**: {query_stats['hits']}\n"
2026-01-26T14:33:47.5278028Z     |
2026-01-26T14:33:47.5278117Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5278128Z 
2026-01-26T14:33:47.5278212Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5278290Z    --> mcp_server.py:844:1
2026-01-26T14:33:47.5278351Z     |
2026-01-26T14:33:47.5278505Z 842 |     result += f"- **Expirations**: {query_stats['expirations']}\n"
2026-01-26T14:33:47.5278632Z 843 |     result += f"- **TTL**: {query_stats['ttl_seconds']}s\n"
2026-01-26T14:33:47.5278876Z 844 |     
2026-01-26T14:33:47.5278944Z     | ^^^^
2026-01-26T14:33:47.5279017Z 845 |     return result
2026-01-26T14:33:47.5279078Z     |
2026-01-26T14:33:47.5279167Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5279172Z 
2026-01-26T14:33:47.5279393Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5279483Z  --> memory_limited_indexer.py:1:1
2026-01-26T14:33:47.5279545Z   |
2026-01-26T14:33:47.5279617Z 1 | / import sys
2026-01-26T14:33:47.5279720Z 2 | | from typing import List, Dict, Any, Callable
2026-01-26T14:33:47.5279800Z 3 | | from logger import get_logger
2026-01-26T14:33:47.5279878Z   | |_____________________________^
2026-01-26T14:33:47.5279937Z 4 |
2026-01-26T14:33:47.5280014Z 5 |   logger = get_logger()
2026-01-26T14:33:47.5280074Z   |
2026-01-26T14:33:47.5280153Z help: Organize imports
2026-01-26T14:33:47.5280158Z 
2026-01-26T14:33:47.5280293Z UP035 [*] Import from `collections.abc` instead: `Callable`
2026-01-26T14:33:47.5280380Z  --> memory_limited_indexer.py:2:1
2026-01-26T14:33:47.5280446Z   |
2026-01-26T14:33:47.5280511Z 1 | import sys
2026-01-26T14:33:47.5280611Z 2 | from typing import List, Dict, Any, Callable
2026-01-26T14:33:47.5280688Z   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5280777Z 3 | from logger import get_logger
2026-01-26T14:33:47.5280837Z   |
2026-01-26T14:33:47.5280925Z help: Import from `collections.abc`
2026-01-26T14:33:47.5280930Z 
2026-01-26T14:33:47.5281054Z UP035 `typing.List` is deprecated, use `list` instead
2026-01-26T14:33:47.5281136Z  --> memory_limited_indexer.py:2:1
2026-01-26T14:33:47.5281195Z   |
2026-01-26T14:33:47.5281264Z 1 | import sys
2026-01-26T14:33:47.5281363Z 2 | from typing import List, Dict, Any, Callable
2026-01-26T14:33:47.5281439Z   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5281518Z 3 | from logger import get_logger
2026-01-26T14:33:47.5281583Z   |
2026-01-26T14:33:47.5281588Z 
2026-01-26T14:33:47.5281703Z UP035 `typing.Dict` is deprecated, use `dict` instead
2026-01-26T14:33:47.5281790Z  --> memory_limited_indexer.py:2:1
2026-01-26T14:33:47.5281855Z   |
2026-01-26T14:33:47.5281919Z 1 | import sys
2026-01-26T14:33:47.5282014Z 2 | from typing import List, Dict, Any, Callable
2026-01-26T14:33:47.5282091Z   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5282177Z 3 | from logger import get_logger
2026-01-26T14:33:47.5282236Z   |
2026-01-26T14:33:47.5282240Z 
2026-01-26T14:33:47.5282323Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5282415Z   --> memory_limited_indexer.py:13:1
2026-01-26T14:33:47.5282475Z    |
2026-01-26T14:33:47.5282645Z 11 |     Automatically flushes batches when memory threshold is reached.
2026-01-26T14:33:47.5282712Z 12 |     """
2026-01-26T14:33:47.5282774Z 13 |     
2026-01-26T14:33:47.5282835Z    | ^^^^
2026-01-26T14:33:47.5283133Z 14 |     def __init__(self, max_memory_bytes: int, batch_callback: Callable[[List[str], List[Dict], List[str]], None]):
2026-01-26T14:33:47.5283201Z 15 |         """
2026-01-26T14:33:47.5283264Z    |
2026-01-26T14:33:47.5283352Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5283357Z 
2026-01-26T14:33:47.5283490Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5283580Z   --> memory_limited_indexer.py:14:73
2026-01-26T14:33:47.5283641Z    |
2026-01-26T14:33:47.5283707Z 12 |     """
2026-01-26T14:33:47.5283771Z 13 |     
2026-01-26T14:33:47.5284053Z 14 |     def __init__(self, max_memory_bytes: int, batch_callback: Callable[[List[str], List[Dict], List[str]], None]):
2026-01-26T14:33:47.5284162Z    |                                                                         ^^^^
2026-01-26T14:33:47.5284231Z 15 |         """
2026-01-26T14:33:47.5284296Z 16 |         Args:
2026-01-26T14:33:47.5284355Z    |
2026-01-26T14:33:47.5284438Z help: Replace with `list`
2026-01-26T14:33:47.5284443Z 
2026-01-26T14:33:47.5284564Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5284649Z   --> memory_limited_indexer.py:14:84
2026-01-26T14:33:47.5284880Z    |
2026-01-26T14:33:47.5284950Z 12 |     """
2026-01-26T14:33:47.5285010Z 13 |     
2026-01-26T14:33:47.5285363Z 14 |     def __init__(self, max_memory_bytes: int, batch_callback: Callable[[List[str], List[Dict], List[str]], None]):
2026-01-26T14:33:47.5285490Z    |                                                                                    ^^^^
2026-01-26T14:33:47.5285552Z 15 |         """
2026-01-26T14:33:47.5285615Z 16 |         Args:
2026-01-26T14:33:47.5285681Z    |
2026-01-26T14:33:47.5285757Z help: Replace with `list`
2026-01-26T14:33:47.5285762Z 
2026-01-26T14:33:47.5285881Z UP006 [*] Use `dict` instead of `Dict` for type annotation
2026-01-26T14:33:47.5285964Z   --> memory_limited_indexer.py:14:89
2026-01-26T14:33:47.5286029Z    |
2026-01-26T14:33:47.5286089Z 12 |     """
2026-01-26T14:33:47.5286149Z 13 |     
2026-01-26T14:33:47.5286427Z 14 |     def __init__(self, max_memory_bytes: int, batch_callback: Callable[[List[str], List[Dict], List[str]], None]):
2026-01-26T14:33:47.5286554Z    |                                                                                         ^^^^
2026-01-26T14:33:47.5286616Z 15 |         """
2026-01-26T14:33:47.5286685Z 16 |         Args:
2026-01-26T14:33:47.5286745Z    |
2026-01-26T14:33:47.5286823Z help: Replace with `dict`
2026-01-26T14:33:47.5286828Z 
2026-01-26T14:33:47.5286944Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5287035Z   --> memory_limited_indexer.py:14:96
2026-01-26T14:33:47.5287094Z    |
2026-01-26T14:33:47.5287154Z 12 |     """
2026-01-26T14:33:47.5287219Z 13 |     
2026-01-26T14:33:47.5287492Z 14 |     def __init__(self, max_memory_bytes: int, batch_callback: Callable[[List[str], List[Dict], List[str]], None]):
2026-01-26T14:33:47.5287626Z    |                                                                                                ^^^^
2026-01-26T14:33:47.5287692Z 15 |         """
2026-01-26T14:33:47.5287757Z 16 |         Args:
2026-01-26T14:33:47.5287819Z    |
2026-01-26T14:33:47.5287895Z help: Replace with `list`
2026-01-26T14:33:47.5287900Z 
2026-01-26T14:33:47.5288021Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5288103Z   --> memory_limited_indexer.py:22:25
2026-01-26T14:33:47.5288166Z    |
2026-01-26T14:33:47.5288272Z 20 |         self.max_memory_bytes = max_memory_bytes
2026-01-26T14:33:47.5288368Z 21 |         self.batch_callback = batch_callback
2026-01-26T14:33:47.5288456Z 22 |         self.documents: List[str] = []
2026-01-26T14:33:47.5288531Z    |                         ^^^^
2026-01-26T14:33:47.5288621Z 23 |         self.metadatas: List[Dict] = []
2026-01-26T14:33:47.5288696Z 24 |         self.ids: List[str] = []
2026-01-26T14:33:47.5288756Z    |
2026-01-26T14:33:47.5288940Z help: Replace with `list`
2026-01-26T14:33:47.5288946Z 
2026-01-26T14:33:47.5289064Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5289148Z   --> memory_limited_indexer.py:23:25
2026-01-26T14:33:47.5289217Z    |
2026-01-26T14:33:47.5289309Z 21 |         self.batch_callback = batch_callback
2026-01-26T14:33:47.5289394Z 22 |         self.documents: List[str] = []
2026-01-26T14:33:47.5289480Z 23 |         self.metadatas: List[Dict] = []
2026-01-26T14:33:47.5289559Z    |                         ^^^^
2026-01-26T14:33:47.5289637Z 24 |         self.ids: List[str] = []
2026-01-26T14:33:47.5289716Z 25 |         self.current_memory = 0
2026-01-26T14:33:47.5289782Z    |
2026-01-26T14:33:47.5289857Z help: Replace with `list`
2026-01-26T14:33:47.5289861Z 
2026-01-26T14:33:47.5289980Z UP006 [*] Use `dict` instead of `Dict` for type annotation
2026-01-26T14:33:47.5290068Z   --> memory_limited_indexer.py:23:30
2026-01-26T14:33:47.5290128Z    |
2026-01-26T14:33:47.5290220Z 21 |         self.batch_callback = batch_callback
2026-01-26T14:33:47.5290305Z 22 |         self.documents: List[str] = []
2026-01-26T14:33:47.5290396Z 23 |         self.metadatas: List[Dict] = []
2026-01-26T14:33:47.5290470Z    |                              ^^^^
2026-01-26T14:33:47.5290700Z 24 |         self.ids: List[str] = []
2026-01-26T14:33:47.5290786Z 25 |         self.current_memory = 0
2026-01-26T14:33:47.5290847Z    |
2026-01-26T14:33:47.5290923Z help: Replace with `dict`
2026-01-26T14:33:47.5290928Z 
2026-01-26T14:33:47.5291339Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5291515Z   --> memory_limited_indexer.py:24:19
2026-01-26T14:33:47.5291620Z    |
2026-01-26T14:33:47.5291780Z 22 |         self.documents: List[str] = []
2026-01-26T14:33:47.5291947Z 23 |         self.metadatas: List[Dict] = []
2026-01-26T14:33:47.5292089Z 24 |         self.ids: List[str] = []
2026-01-26T14:33:47.5292209Z    |                   ^^^^
2026-01-26T14:33:47.5292354Z 25 |         self.current_memory = 0
2026-01-26T14:33:47.5292486Z 26 |         self.total_chunks = 0
2026-01-26T14:33:47.5292590Z    |
2026-01-26T14:33:47.5292726Z help: Replace with `list`
2026-01-26T14:33:47.5292746Z 
2026-01-26T14:33:47.5292894Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5293052Z   --> memory_limited_indexer.py:28:1
2026-01-26T14:33:47.5293160Z    |
2026-01-26T14:33:47.5293303Z 26 |         self.total_chunks = 0
2026-01-26T14:33:47.5293445Z 27 |         self.total_batches = 0
2026-01-26T14:33:47.5293575Z 28 |     
2026-01-26T14:33:47.5293649Z    | ^^^^
2026-01-26T14:33:47.5293766Z 29 |     def _estimate_size(self, obj: Any) -> int:
2026-01-26T14:33:47.5293828Z 30 |         """
2026-01-26T14:33:47.5293886Z    |
2026-01-26T14:33:47.5293983Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5293988Z 
2026-01-26T14:33:47.5294072Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5294158Z   --> memory_limited_indexer.py:35:1
2026-01-26T14:33:47.5294223Z    |
2026-01-26T14:33:47.5294282Z 33 |         """
2026-01-26T14:33:47.5294363Z 34 |         size = sys.getsizeof(obj)
2026-01-26T14:33:47.5294424Z 35 |         
2026-01-26T14:33:47.5294489Z    | ^^^^^^^^
2026-01-26T14:33:47.5294655Z 36 |         if isinstance(obj, dict):
2026-01-26T14:33:47.5294860Z 37 |             size += sum(sys.getsizeof(k) + sys.getsizeof(v) for k, v in obj.items())
2026-01-26T14:33:47.5294925Z    |
2026-01-26T14:33:47.5295013Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5295018Z 
2026-01-26T14:33:47.5295101Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5295196Z   --> memory_limited_indexer.py:40:1
2026-01-26T14:33:47.5295255Z    |
2026-01-26T14:33:47.5295352Z 38 |         elif isinstance(obj, (list, tuple)):
2026-01-26T14:33:47.5295476Z 39 |             size += sum(sys.getsizeof(item) for item in obj)
2026-01-26T14:33:47.5295541Z 40 |         
2026-01-26T14:33:47.5295599Z    | ^^^^^^^^
2026-01-26T14:33:47.5295669Z 41 |         return size
2026-01-26T14:33:47.5295732Z    |
2026-01-26T14:33:47.5295818Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5295824Z 
2026-01-26T14:33:47.5295903Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5295984Z   --> memory_limited_indexer.py:42:1
2026-01-26T14:33:47.5296051Z    |
2026-01-26T14:33:47.5296119Z 41 |         return size
2026-01-26T14:33:47.5296177Z 42 |     
2026-01-26T14:33:47.5296240Z    | ^^^^
2026-01-26T14:33:47.5296448Z 43 |     def add_chunk(self, document: str, metadata: Dict[str, Any], doc_id: str) -> None:
2026-01-26T14:33:47.5296512Z 44 |         """
2026-01-26T14:33:47.5296570Z    |
2026-01-26T14:33:47.5296659Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5296664Z 
2026-01-26T14:33:47.5296790Z UP006 [*] Use `dict` instead of `Dict` for type annotation
2026-01-26T14:33:47.5296876Z   --> memory_limited_indexer.py:43:50
2026-01-26T14:33:47.5296941Z    |
2026-01-26T14:33:47.5297008Z 41 |         return size
2026-01-26T14:33:47.5297067Z 42 |     
2026-01-26T14:33:47.5297270Z 43 |     def add_chunk(self, document: str, metadata: Dict[str, Any], doc_id: str) -> None:
2026-01-26T14:33:47.5297359Z    |                                                  ^^^^
2026-01-26T14:33:47.5297419Z 44 |         """
2026-01-26T14:33:47.5297576Z 45 |         Adds a chunk to the buffer. Flushes if memory limit exceeded.
2026-01-26T14:33:47.5297760Z    |
2026-01-26T14:33:47.5297839Z help: Replace with `dict`
2026-01-26T14:33:47.5297844Z 
2026-01-26T14:33:47.5297928Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5298087Z   --> memory_limited_indexer.py:46:1
2026-01-26T14:33:47.5298148Z    |
2026-01-26T14:33:47.5298208Z 44 |         """
2026-01-26T14:33:47.5298364Z 45 |         Adds a chunk to the buffer. Flushes if memory limit exceeded.
2026-01-26T14:33:47.5298425Z 46 |         
2026-01-26T14:33:47.5298483Z    | ^^^^^^^^
2026-01-26T14:33:47.5298546Z 47 |         Args:
2026-01-26T14:33:47.5298638Z 48 |             document: Document text
2026-01-26T14:33:47.5298696Z    |
2026-01-26T14:33:47.5298989Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5299000Z 
2026-01-26T14:33:47.5299140Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5299227Z   --> memory_limited_indexer.py:57:1
2026-01-26T14:33:47.5299287Z    |
2026-01-26T14:33:47.5299382Z 55 |             self._estimate_size(doc_id)
2026-01-26T14:33:47.5299448Z 56 |         )
2026-01-26T14:33:47.5299507Z 57 |         
2026-01-26T14:33:47.5299565Z    | ^^^^^^^^
2026-01-26T14:33:47.5299783Z 58 |         if self.current_memory + chunk_size > self.max_memory_bytes and self.documents:
2026-01-26T14:33:47.5299865Z 59 |             self.flush()
2026-01-26T14:33:47.5299924Z    |
2026-01-26T14:33:47.5300013Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5300018Z 
2026-01-26T14:33:47.5300099Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5300181Z   --> memory_limited_indexer.py:60:1
2026-01-26T14:33:47.5300241Z    |
2026-01-26T14:33:47.5300449Z 58 |         if self.current_memory + chunk_size > self.max_memory_bytes and self.documents:
2026-01-26T14:33:47.5300519Z 59 |             self.flush()
2026-01-26T14:33:47.5300578Z 60 |         
2026-01-26T14:33:47.5300641Z    | ^^^^^^^^
2026-01-26T14:33:47.5300737Z 61 |         self.documents.append(document)
2026-01-26T14:33:47.5300831Z 62 |         self.metadatas.append(metadata)
2026-01-26T14:33:47.5300889Z    |
2026-01-26T14:33:47.5300980Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5300985Z 
2026-01-26T14:33:47.5301067Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5301151Z   --> memory_limited_indexer.py:66:1
2026-01-26T14:33:47.5301216Z    |
2026-01-26T14:33:47.5301306Z 64 |         self.current_memory += chunk_size
2026-01-26T14:33:47.5301384Z 65 |         self.total_chunks += 1
2026-01-26T14:33:47.5301448Z 66 |     
2026-01-26T14:33:47.5301506Z    | ^^^^
2026-01-26T14:33:47.5301582Z 67 |     def flush(self) -> None:
2026-01-26T14:33:47.5301645Z 68 |         """
2026-01-26T14:33:47.5301709Z    |
2026-01-26T14:33:47.5301792Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5301796Z 
2026-01-26T14:33:47.5301881Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5301965Z   --> memory_limited_indexer.py:74:1
2026-01-26T14:33:47.5302023Z    |
2026-01-26T14:33:47.5302098Z 72 |         if not self.documents:
2026-01-26T14:33:47.5302168Z 73 |             return
2026-01-26T14:33:47.5302246Z 74 |         
2026-01-26T14:33:47.5302309Z    | ^^^^^^^^
2026-01-26T14:33:47.5302381Z 75 |         logger.debug(
2026-01-26T14:33:47.5302511Z 76 |             f"Flushing batch {self.total_batches + 1}: "
2026-01-26T14:33:47.5302570Z    |
2026-01-26T14:33:47.5302656Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5302660Z 
2026-01-26T14:33:47.5302747Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5302838Z   --> memory_limited_indexer.py:80:1
2026-01-26T14:33:47.5302897Z    |
2026-01-26T14:33:47.5303009Z 78 |             f"{self.current_memory / 1024 / 1024:.2f} MB"
2026-01-26T14:33:47.5303075Z 79 |         )
2026-01-26T14:33:47.5303134Z 80 |         
2026-01-26T14:33:47.5303192Z    | ^^^^^^^^
2026-01-26T14:33:47.5303261Z 81 |         try:
2026-01-26T14:33:47.5303429Z 82 |             self.batch_callback(self.documents, self.metadatas, self.ids)
2026-01-26T14:33:47.5303497Z    |
2026-01-26T14:33:47.5303737Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5303742Z 
2026-01-26T14:33:47.5303827Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5303919Z   --> memory_limited_indexer.py:92:1
2026-01-26T14:33:47.5303979Z    |
2026-01-26T14:33:47.5304160Z 90 |             self.ids.clear()
2026-01-26T14:33:47.5304245Z 91 |             self.current_memory = 0
2026-01-26T14:33:47.5304304Z 92 |     
2026-01-26T14:33:47.5304363Z    | ^^^^
2026-01-26T14:33:47.5304464Z 93 |     def get_stats(self) -> Dict[str, Any]:
2026-01-26T14:33:47.5304524Z 94 |         """
2026-01-26T14:33:47.5304583Z    |
2026-01-26T14:33:47.5304673Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5304678Z 
2026-01-26T14:33:47.5304802Z UP006 [*] Use `dict` instead of `Dict` for type annotation
2026-01-26T14:33:47.5304887Z   --> memory_limited_indexer.py:93:28
2026-01-26T14:33:47.5304949Z    |
2026-01-26T14:33:47.5305028Z 91 |             self.current_memory = 0
2026-01-26T14:33:47.5305099Z 92 |     
2026-01-26T14:33:47.5305190Z 93 |     def get_stats(self) -> Dict[str, Any]:
2026-01-26T14:33:47.5305266Z    |                            ^^^^
2026-01-26T14:33:47.5305327Z 94 |         """
2026-01-26T14:33:47.5305411Z 95 |         Returns indexing statistics.
2026-01-26T14:33:47.5305477Z    |
2026-01-26T14:33:47.5305553Z help: Replace with `dict`
2026-01-26T14:33:47.5305558Z 
2026-01-26T14:33:47.5305635Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5305723Z   --> memory_limited_indexer.py:96:1
2026-01-26T14:33:47.5305781Z    |
2026-01-26T14:33:47.5305840Z 94 |         """
2026-01-26T14:33:47.5305923Z 95 |         Returns indexing statistics.
2026-01-26T14:33:47.5305992Z 96 |         
2026-01-26T14:33:47.5306052Z    | ^^^^^^^^
2026-01-26T14:33:47.5306117Z 97 |         Returns:
2026-01-26T14:33:47.5306291Z 98 |             Dictionary with total_chunks, total_batches, current_buffer_size
2026-01-26T14:33:47.5306350Z    |
2026-01-26T14:33:47.5306449Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5306457Z 
2026-01-26T14:33:47.5306563Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5306648Z   --> memory_manager.py:1:1
2026-01-26T14:33:47.5306710Z    |
2026-01-26T14:33:47.5306776Z  1 | / import json
2026-01-26T14:33:47.5306853Z  2 | | import shutil
2026-01-26T14:33:47.5306934Z  3 | | from pathlib import Path
2026-01-26T14:33:47.5307014Z  4 | | from datetime import datetime
2026-01-26T14:33:47.5307100Z  5 | | from typing import Optional, List
2026-01-26T14:33:47.5307169Z  6 | |
2026-01-26T14:33:47.5307360Z  7 | | from config import MEMORY_FILE, MEMORY_HISTORY_DIR
2026-01-26T14:33:47.5307508Z  8 | | from logger import get_logger
2026-01-26T14:33:47.5307646Z    | |_____________________________^
2026-01-26T14:33:47.5307751Z  9 |
2026-01-26T14:33:47.5307889Z 10 |   logger = get_logger()
2026-01-26T14:33:47.5307992Z    |
2026-01-26T14:33:47.5308130Z help: Organize imports
2026-01-26T14:33:47.5308139Z 
2026-01-26T14:33:47.5308354Z UP035 `typing.List` is deprecated, use `list` instead
2026-01-26T14:33:47.5308505Z  --> memory_manager.py:5:1
2026-01-26T14:33:47.5308624Z   |
2026-01-26T14:33:47.5308937Z 3 | from pathlib import Path
2026-01-26T14:33:47.5309094Z 4 | from datetime import datetime
2026-01-26T14:33:47.5309258Z 5 | from typing import Optional, List
2026-01-26T14:33:47.5309376Z   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5309472Z 6 |
2026-01-26T14:33:47.5309667Z 7 | from config import MEMORY_FILE, MEMORY_HISTORY_DIR
2026-01-26T14:33:47.5309783Z   |
2026-01-26T14:33:47.5309791Z 
2026-01-26T14:33:47.5309964Z F401 [*] `typing.Optional` imported but unused
2026-01-26T14:33:47.5310089Z  --> memory_manager.py:5:20
2026-01-26T14:33:47.5310185Z   |
2026-01-26T14:33:47.5310309Z 3 | from pathlib import Path
2026-01-26T14:33:47.5310434Z 4 | from datetime import datetime
2026-01-26T14:33:47.5310568Z 5 | from typing import Optional, List
2026-01-26T14:33:47.5310685Z   |                    ^^^^^^^^
2026-01-26T14:33:47.5310788Z 6 |
2026-01-26T14:33:47.5310979Z 7 | from config import MEMORY_FILE, MEMORY_HISTORY_DIR
2026-01-26T14:33:47.5311283Z   |
2026-01-26T14:33:47.5311418Z help: Remove unused import
2026-01-26T14:33:47.5311427Z 
2026-01-26T14:33:47.5311583Z F401 [*] `typing.List` imported but unused
2026-01-26T14:33:47.5311871Z  --> memory_manager.py:5:30
2026-01-26T14:33:47.5311965Z   |
2026-01-26T14:33:47.5312053Z 3 | from pathlib import Path
2026-01-26T14:33:47.5312234Z 4 | from datetime import datetime
2026-01-26T14:33:47.5312339Z 5 | from typing import Optional, List
2026-01-26T14:33:47.5312408Z   |                              ^^^^
2026-01-26T14:33:47.5312467Z 6 |
2026-01-26T14:33:47.5312594Z 7 | from config import MEMORY_FILE, MEMORY_HISTORY_DIR
2026-01-26T14:33:47.5312653Z   |
2026-01-26T14:33:47.5312733Z help: Remove unused import
2026-01-26T14:33:47.5312738Z 
2026-01-26T14:33:47.5312826Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5312912Z   --> memory_manager.py:18:1
2026-01-26T14:33:47.5312970Z    |
2026-01-26T14:33:47.5313144Z 16 |     Encapsulates reading, updating, versioning of memory.md file.
2026-01-26T14:33:47.5313216Z 17 |     """
2026-01-26T14:33:47.5313276Z 18 |     
2026-01-26T14:33:47.5313334Z    | ^^^^
2026-01-26T14:33:47.5313472Z 19 |     def __init__(self, memory_file: Path = MEMORY_FILE):
2026-01-26T14:33:47.5313541Z 20 |         """
2026-01-26T14:33:47.5313608Z    |
2026-01-26T14:33:47.5313700Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5313705Z 
2026-01-26T14:33:47.5313792Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5313869Z   --> memory_manager.py:22:1
2026-01-26T14:33:47.5313927Z    |
2026-01-26T14:33:47.5313994Z 20 |         """
2026-01-26T14:33:47.5314074Z 21 |         Initialize memory manager.
2026-01-26T14:33:47.5314134Z 22 |         
2026-01-26T14:33:47.5314193Z    | ^^^^^^^^
2026-01-26T14:33:47.5314263Z 23 |         Args:
2026-01-26T14:33:47.5314358Z 24 |             memory_file: Path to memory file
2026-01-26T14:33:47.5314416Z    |
2026-01-26T14:33:47.5314506Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5314515Z 
2026-01-26T14:33:47.5314597Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5314677Z   --> memory_manager.py:28:1
2026-01-26T14:33:47.5314734Z    |
2026-01-26T14:33:47.5314826Z 26 |         self.memory_file = memory_file
2026-01-26T14:33:47.5314927Z 27 |         self.history_dir = MEMORY_HISTORY_DIR
2026-01-26T14:33:47.5314988Z 28 |     
2026-01-26T14:33:47.5315051Z    | ^^^^
2026-01-26T14:33:47.5315129Z 29 |     def read(self) -> str:
2026-01-26T14:33:47.5315189Z 30 |         """
2026-01-26T14:33:47.5315251Z    |
2026-01-26T14:33:47.5315335Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5315340Z 
2026-01-26T14:33:47.5315421Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5315498Z   --> memory_manager.py:32:1
2026-01-26T14:33:47.5315562Z    |
2026-01-26T14:33:47.5315621Z 30 |         """
2026-01-26T14:33:47.5315707Z 31 |         Reads current memory content.
2026-01-26T14:33:47.5315775Z 32 |         
2026-01-26T14:33:47.5315834Z    | ^^^^^^^^
2026-01-26T14:33:47.5315903Z 33 |         Returns:
2026-01-26T14:33:47.5315992Z 34 |             Memory content or error message
2026-01-26T14:33:47.5316059Z    |
2026-01-26T14:33:47.5316144Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5316149Z 
2026-01-26T14:33:47.5316231Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5316313Z   --> memory_manager.py:38:1
2026-01-26T14:33:47.5316371Z    |
2026-01-26T14:33:47.5316463Z 36 |         if not self.memory_file.exists():
2026-01-26T14:33:47.5316551Z 37 |             return "Memory file not found."
2026-01-26T14:33:47.5316616Z 38 |         
2026-01-26T14:33:47.5316674Z    | ^^^^^^^^
2026-01-26T14:33:47.5316736Z 39 |         try:
2026-01-26T14:33:47.5316842Z 40 |             return self.memory_file.read_text()
2026-01-26T14:33:47.5316900Z    |
2026-01-26T14:33:47.5316985Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5316989Z 
2026-01-26T14:33:47.5317074Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5317241Z   --> memory_manager.py:44:1
2026-01-26T14:33:47.5317300Z    |
2026-01-26T14:33:47.5317414Z 42 |             logger.error(f"Error reading memory: {e}")
2026-01-26T14:33:47.5317515Z 43 |             return f"Error reading memory: {e}"
2026-01-26T14:33:47.5317648Z 44 |     
2026-01-26T14:33:47.5317709Z    | ^^^^
2026-01-26T14:33:47.5317904Z 45 |     def update(self, content: str, section: str = "Recent Decisions") -> str:
2026-01-26T14:33:47.5317966Z 46 |         """
2026-01-26T14:33:47.5318023Z    |
2026-01-26T14:33:47.5318109Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5318120Z 
2026-01-26T14:33:47.5318199Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5318278Z   --> memory_manager.py:48:1
2026-01-26T14:33:47.5318336Z    |
2026-01-26T14:33:47.5318405Z 46 |         """
2026-01-26T14:33:47.5318498Z 47 |         Appends new content to memory file.
2026-01-26T14:33:47.5318559Z 48 |         
2026-01-26T14:33:47.5318621Z    | ^^^^^^^^
2026-01-26T14:33:47.5318683Z 49 |         Args:
2026-01-26T14:33:47.5319022Z 50 |             content: Content to append
2026-01-26T14:33:47.5319139Z    |
2026-01-26T14:33:47.5319249Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5319256Z 
2026-01-26T14:33:47.5319340Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5319424Z   --> memory_manager.py:52:1
2026-01-26T14:33:47.5319488Z    |
2026-01-26T14:33:47.5319574Z 50 |             content: Content to append
2026-01-26T14:33:47.5319674Z 51 |             section: Section name for the update
2026-01-26T14:33:47.5319737Z 52 |             
2026-01-26T14:33:47.5319803Z    | ^^^^^^^^^^^^
2026-01-26T14:33:47.5319868Z 53 |         Returns:
2026-01-26T14:33:47.5319951Z 54 |             Success message or error
2026-01-26T14:33:47.5320016Z    |
2026-01-26T14:33:47.5320103Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5320108Z 
2026-01-26T14:33:47.5320189Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5320274Z   --> memory_manager.py:58:1
2026-01-26T14:33:47.5320335Z    |
2026-01-26T14:33:47.5320427Z 56 |         if not self.memory_file.exists():
2026-01-26T14:33:47.5320516Z 57 |             return "Memory file not found."
2026-01-26T14:33:47.5320581Z 58 |         
2026-01-26T14:33:47.5320641Z    | ^^^^^^^^
2026-01-26T14:33:47.5320742Z 59 |         if not content or not content.strip():
2026-01-26T14:33:47.5320857Z 60 |             return "Error: Content cannot be empty."
2026-01-26T14:33:47.5320915Z    |
2026-01-26T14:33:47.5321010Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5321015Z 
2026-01-26T14:33:47.5321098Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5321183Z   --> memory_manager.py:61:1
2026-01-26T14:33:47.5321244Z    |
2026-01-26T14:33:47.5321342Z 59 |         if not content or not content.strip():
2026-01-26T14:33:47.5326761Z 60 |             return "Error: Content cannot be empty."
2026-01-26T14:33:47.5326840Z 61 |         
2026-01-26T14:33:47.5326901Z    | ^^^^^^^^
2026-01-26T14:33:47.5326968Z 62 |         try:
2026-01-26T14:33:47.5327122Z 63 |             new_entry = f"\n\n### Update ({section})\n{content}"
2026-01-26T14:33:47.5327184Z    |
2026-01-26T14:33:47.5327281Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5327287Z 
2026-01-26T14:33:47.5327383Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5327469Z   --> memory_manager.py:64:1
2026-01-26T14:33:47.5327527Z    |
2026-01-26T14:33:47.5327597Z 62 |         try:
2026-01-26T14:33:47.5327731Z 63 |             new_entry = f"\n\n### Update ({section})\n{content}"
2026-01-26T14:33:47.5327792Z 64 |             
2026-01-26T14:33:47.5327851Z    | ^^^^^^^^^^^^
2026-01-26T14:33:47.5327969Z 65 |             with open(self.memory_file, "a") as f:
2026-01-26T14:33:47.5328049Z 66 |                 f.write(new_entry)
2026-01-26T14:33:47.5328107Z    |
2026-01-26T14:33:47.5328201Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5328206Z 
2026-01-26T14:33:47.5328292Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5328375Z   --> memory_manager.py:67:1
2026-01-26T14:33:47.5328630Z    |
2026-01-26T14:33:47.5328736Z 65 |             with open(self.memory_file, "a") as f:
2026-01-26T14:33:47.5329067Z 66 |                 f.write(new_entry)
2026-01-26T14:33:47.5329139Z 67 |             
2026-01-26T14:33:47.5329345Z    | ^^^^^^^^^^^^
2026-01-26T14:33:47.5329476Z 68 |             logger.info(f"Memory updated: {section}")
2026-01-26T14:33:47.5329583Z 69 |             return "Memory updated successfully."
2026-01-26T14:33:47.5329646Z    |
2026-01-26T14:33:47.5329732Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5329738Z 
2026-01-26T14:33:47.5329820Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5329905Z   --> memory_manager.py:73:1
2026-01-26T14:33:47.5329962Z    |
2026-01-26T14:33:47.5330079Z 71 |             logger.error(f"Error updating memory: {e}")
2026-01-26T14:33:47.5330180Z 72 |             return f"Error updating memory: {e}"
2026-01-26T14:33:47.5330244Z 73 |     
2026-01-26T14:33:47.5330304Z    | ^^^^
2026-01-26T14:33:47.5330440Z 74 |     def clear(self, keep_template: bool = True) -> str:
2026-01-26T14:33:47.5330507Z 75 |         """
2026-01-26T14:33:47.5330567Z    |
2026-01-26T14:33:47.5330657Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5330662Z 
2026-01-26T14:33:47.5330747Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5330830Z   --> memory_manager.py:77:1
2026-01-26T14:33:47.5330888Z    |
2026-01-26T14:33:47.5330948Z 75 |         """
2026-01-26T14:33:47.5331042Z 76 |         Clears memory file content.
2026-01-26T14:33:47.5331102Z 77 |         
2026-01-26T14:33:47.5331160Z    | ^^^^^^^^
2026-01-26T14:33:47.5331223Z 78 |         Args:
2026-01-26T14:33:47.5331370Z 79 |             keep_template: If True, preserves template structure
2026-01-26T14:33:47.5331428Z    |
2026-01-26T14:33:47.5331518Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5331523Z 
2026-01-26T14:33:47.5331613Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5331691Z   --> memory_manager.py:80:1
2026-01-26T14:33:47.5331752Z    |
2026-01-26T14:33:47.5331820Z 78 |         Args:
2026-01-26T14:33:47.5331958Z 79 |             keep_template: If True, preserves template structure
2026-01-26T14:33:47.5332018Z 80 |             
2026-01-26T14:33:47.5332079Z    | ^^^^^^^^^^^^
2026-01-26T14:33:47.5332154Z 81 |         Returns:
2026-01-26T14:33:47.5332237Z 82 |             Success message or error
2026-01-26T14:33:47.5332294Z    |
2026-01-26T14:33:47.5332385Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5332390Z 
2026-01-26T14:33:47.5332472Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5332553Z   --> memory_manager.py:86:1
2026-01-26T14:33:47.5332611Z    |
2026-01-26T14:33:47.5332710Z 84 |         if not self.memory_file.exists():
2026-01-26T14:33:47.5332801Z 85 |             return "Memory file not found."
2026-01-26T14:33:47.5332861Z 86 |         
2026-01-26T14:33:47.5332926Z    | ^^^^^^^^
2026-01-26T14:33:47.5332988Z 87 |         try:
2026-01-26T14:33:47.5333064Z 88 |             if keep_template:
2026-01-26T14:33:47.5333128Z    |
2026-01-26T14:33:47.5333214Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5333219Z 
2026-01-26T14:33:47.5333292Z W291 Trailing whitespace
2026-01-26T14:33:47.5333372Z   --> memory_manager.py:96:13
2026-01-26T14:33:47.5333439Z    |
2026-01-26T14:33:47.5333503Z 94 | ## Tech Stack
2026-01-26T14:33:47.5333577Z 95 | - Language: Python
2026-01-26T14:33:47.5333651Z 96 | - Framework: 
2026-01-26T14:33:47.5333710Z    |             ^
2026-01-26T14:33:47.5333767Z 97 |
2026-01-26T14:33:47.5333837Z 98 | ## Recent Decisions
2026-01-26T14:33:47.5333900Z    |
2026-01-26T14:33:47.5333984Z help: Remove trailing whitespace
2026-01-26T14:33:47.5333989Z 
2026-01-26T14:33:47.5334070Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5334159Z    --> memory_manager.py:111:1
2026-01-26T14:33:47.5334219Z     |
2026-01-26T14:33:47.5334347Z 109 |             logger.error(f"Error clearing memory: {e}")
2026-01-26T14:33:47.5334451Z 110 |             return f"Error clearing memory: {e}"
2026-01-26T14:33:47.5334636Z 111 |     
2026-01-26T14:33:47.5334695Z     | ^^^^
2026-01-26T14:33:47.5334827Z 112 |     def delete_section(self, section_name: str) -> str:
2026-01-26T14:33:47.5334893Z 113 |         """
2026-01-26T14:33:47.5334953Z     |
2026-01-26T14:33:47.5335114Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5335120Z 
2026-01-26T14:33:47.5335208Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5335299Z    --> memory_manager.py:115:1
2026-01-26T14:33:47.5335359Z     |
2026-01-26T14:33:47.5335418Z 113 |         """
2026-01-26T14:33:47.5335533Z 114 |         Deletes a specific section from memory.
2026-01-26T14:33:47.5335593Z 115 |         
2026-01-26T14:33:47.5335652Z     | ^^^^^^^^
2026-01-26T14:33:47.5335722Z 116 |         Args:
2026-01-26T14:33:47.5335829Z 117 |             section_name: Name of section to delete
2026-01-26T14:33:47.5335885Z     |
2026-01-26T14:33:47.5335972Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5335982Z 
2026-01-26T14:33:47.5336067Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5336144Z    --> memory_manager.py:118:1
2026-01-26T14:33:47.5336200Z     |
2026-01-26T14:33:47.5336266Z 116 |         Args:
2026-01-26T14:33:47.5336372Z 117 |             section_name: Name of section to delete
2026-01-26T14:33:47.5336432Z 118 |             
2026-01-26T14:33:47.5336500Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5336564Z 119 |         Returns:
2026-01-26T14:33:47.5336649Z 120 |             Success message or error
2026-01-26T14:33:47.5336707Z     |
2026-01-26T14:33:47.5336798Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5336804Z 
2026-01-26T14:33:47.5336885Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5336961Z    --> memory_manager.py:124:1
2026-01-26T14:33:47.5337023Z     |
2026-01-26T14:33:47.5337121Z 122 |         if not self.memory_file.exists():
2026-01-26T14:33:47.5337213Z 123 |             return "Memory file not found."
2026-01-26T14:33:47.5337275Z 124 |         
2026-01-26T14:33:47.5337343Z     | ^^^^^^^^
2026-01-26T14:33:47.5337467Z 125 |         if not section_name or not section_name.strip():
2026-01-26T14:33:47.5337588Z 126 |             return "Error: Section name cannot be empty."
2026-01-26T14:33:47.5337652Z     |
2026-01-26T14:33:47.5337740Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5337744Z 
2026-01-26T14:33:47.5337825Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5337909Z    --> memory_manager.py:127:1
2026-01-26T14:33:47.5337968Z     |
2026-01-26T14:33:47.5338085Z 125 |         if not section_name or not section_name.strip():
2026-01-26T14:33:47.5338198Z 126 |             return "Error: Section name cannot be empty."
2026-01-26T14:33:47.5338267Z 127 |         
2026-01-26T14:33:47.5338326Z     | ^^^^^^^^
2026-01-26T14:33:47.5338387Z 128 |         try:
2026-01-26T14:33:47.5338500Z 129 |             content = self.memory_file.read_text()
2026-01-26T14:33:47.5338559Z     |
2026-01-26T14:33:47.5338643Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5338651Z 
2026-01-26T14:33:47.5338735Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5339015Z    --> memory_manager.py:133:1
2026-01-26T14:33:47.5339077Z     |
2026-01-26T14:33:47.5339151Z 131 |             new_lines = []
2026-01-26T14:33:47.5339242Z 132 |             skip = False
2026-01-26T14:33:47.5339309Z 133 |             
2026-01-26T14:33:47.5339368Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5339450Z 134 |             for line in lines:
2026-01-26T14:33:47.5339644Z 135 |                 if line.startswith("##") and section_name.lower() in line.lower():
2026-01-26T14:33:47.5339710Z     |
2026-01-26T14:33:47.5339795Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5339800Z 
2026-01-26T14:33:47.5339887Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5339964Z    --> memory_manager.py:140:1
2026-01-26T14:33:47.5340021Z     |
2026-01-26T14:33:47.5340131Z 138 |                 elif line.startswith("##") and skip:
2026-01-26T14:33:47.5340206Z 139 |                     skip = False
2026-01-26T14:33:47.5340476Z 140 |                 
2026-01-26T14:33:47.5340546Z     | ^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5340620Z 141 |                 if not skip:
2026-01-26T14:33:47.5340714Z 142 |                     new_lines.append(line)
2026-01-26T14:33:47.5340871Z     |
2026-01-26T14:33:47.5340967Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5340972Z 
2026-01-26T14:33:47.5341058Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5341158Z    --> memory_manager.py:143:1
2026-01-26T14:33:47.5341223Z     |
2026-01-26T14:33:47.5341291Z 141 |                 if not skip:
2026-01-26T14:33:47.5341380Z 142 |                     new_lines.append(line)
2026-01-26T14:33:47.5341440Z 143 |             
2026-01-26T14:33:47.5341505Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5341639Z 144 |             self.memory_file.write_text("\n".join(new_lines))
2026-01-26T14:33:47.5341779Z 145 |             logger.info(f"Section '{section_name}' deleted")
2026-01-26T14:33:47.5341855Z     |
2026-01-26T14:33:47.5341939Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5341944Z 
2026-01-26T14:33:47.5342025Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5342106Z    --> memory_manager.py:150:1
2026-01-26T14:33:47.5342165Z     |
2026-01-26T14:33:47.5342284Z 148 |             logger.error(f"Error deleting section: {e}")
2026-01-26T14:33:47.5342389Z 149 |             return f"Error deleting section: {e}"
2026-01-26T14:33:47.5342454Z 150 |     
2026-01-26T14:33:47.5342513Z     | ^^^^
2026-01-26T14:33:47.5342642Z 151 |     def save_version(self, description: str = "") -> str:
2026-01-26T14:33:47.5342709Z 152 |         """
2026-01-26T14:33:47.5342766Z     |
2026-01-26T14:33:47.5342848Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5342853Z 
2026-01-26T14:33:47.5342937Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5343013Z    --> memory_manager.py:154:1
2026-01-26T14:33:47.5343072Z     |
2026-01-26T14:33:47.5343134Z 152 |         """
2026-01-26T14:33:47.5343260Z 153 |         Saves a versioned copy of the current memory.
2026-01-26T14:33:47.5343320Z 154 |         
2026-01-26T14:33:47.5343381Z     | ^^^^^^^^
2026-01-26T14:33:47.5343448Z 155 |         Args:
2026-01-26T14:33:47.5343586Z 156 |             description: Optional description of this version
2026-01-26T14:33:47.5343646Z     |
2026-01-26T14:33:47.5343730Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5343735Z 
2026-01-26T14:33:47.5343819Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5343894Z    --> memory_manager.py:157:1
2026-01-26T14:33:47.5343951Z     |
2026-01-26T14:33:47.5344017Z 155 |         Args:
2026-01-26T14:33:47.5344141Z 156 |             description: Optional description of this version
2026-01-26T14:33:47.5344202Z 157 |             
2026-01-26T14:33:47.5344261Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5344335Z 158 |         Returns:
2026-01-26T14:33:47.5344462Z 159 |             Success message with version name or error
2026-01-26T14:33:47.5344522Z     |
2026-01-26T14:33:47.5344617Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5344621Z 
2026-01-26T14:33:47.5344702Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5344779Z    --> memory_manager.py:163:1
2026-01-26T14:33:47.5344842Z     |
2026-01-26T14:33:47.5344939Z 161 |         if not self.memory_file.exists():
2026-01-26T14:33:47.5345029Z 162 |             return "Memory file not found"
2026-01-26T14:33:47.5345089Z 163 |         
2026-01-26T14:33:47.5345153Z     | ^^^^^^^^
2026-01-26T14:33:47.5345215Z 164 |         try:
2026-01-26T14:33:47.5345363Z 165 |             self.history_dir.mkdir(parents=True, exist_ok=True)
2026-01-26T14:33:47.5345427Z     |
2026-01-26T14:33:47.5345516Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5345521Z 
2026-01-26T14:33:47.5345601Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5345685Z    --> memory_manager.py:166:1
2026-01-26T14:33:47.5345744Z     |
2026-01-26T14:33:47.5345806Z 164 |         try:
2026-01-26T14:33:47.5346028Z 165 |             self.history_dir.mkdir(parents=True, exist_ok=True)
2026-01-26T14:33:47.5346097Z 166 |             
2026-01-26T14:33:47.5346156Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5346290Z 167 |             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
2026-01-26T14:33:47.5346531Z 168 |             version_file = self.history_dir / f"memory_{timestamp}.md"
2026-01-26T14:33:47.5346592Z     |
2026-01-26T14:33:47.5346680Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5346684Z 
2026-01-26T14:33:47.5346768Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5346843Z    --> memory_manager.py:169:1
2026-01-26T14:33:47.5346901Z     |
2026-01-26T14:33:47.5347031Z 167 |             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
2026-01-26T14:33:47.5347182Z 168 |             version_file = self.history_dir / f"memory_{timestamp}.md"
2026-01-26T14:33:47.5347241Z 169 |             
2026-01-26T14:33:47.5347299Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5347420Z 170 |             shutil.copy2(self.memory_file, version_file)
2026-01-26T14:33:47.5347483Z     |
2026-01-26T14:33:47.5347567Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5347572Z 
2026-01-26T14:33:47.5347652Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5347734Z    --> memory_manager.py:171:1
2026-01-26T14:33:47.5347791Z     |
2026-01-26T14:33:47.5347903Z 170 |             shutil.copy2(self.memory_file, version_file)
2026-01-26T14:33:47.5347968Z 171 |             
2026-01-26T14:33:47.5348026Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5348199Z 172 |             metadata_file = self.history_dir / f"memory_{timestamp}.meta.json"
2026-01-26T14:33:47.5348273Z 173 |             metadata = {
2026-01-26T14:33:47.5348332Z     |
2026-01-26T14:33:47.5348416Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5348421Z 
2026-01-26T14:33:47.5348499Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5348579Z    --> memory_manager.py:178:1
2026-01-26T14:33:47.5348637Z     |
2026-01-26T14:33:47.5348751Z 176 |                 "created_at": datetime.now().isoformat(),
2026-01-26T14:33:47.5349107Z 177 |             }
2026-01-26T14:33:47.5349179Z 178 |             
2026-01-26T14:33:47.5349239Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5349359Z 179 |             with open(metadata_file, "w") as f:
2026-01-26T14:33:47.5349471Z 180 |                 json.dump(metadata, f, indent=2)
2026-01-26T14:33:47.5349531Z     |
2026-01-26T14:33:47.5349617Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5349622Z 
2026-01-26T14:33:47.5349711Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5349789Z    --> memory_manager.py:181:1
2026-01-26T14:33:47.5349848Z     |
2026-01-26T14:33:47.5349948Z 179 |             with open(metadata_file, "w") as f:
2026-01-26T14:33:47.5350044Z 180 |                 json.dump(metadata, f, indent=2)
2026-01-26T14:33:47.5350104Z 181 |             
2026-01-26T14:33:47.5350162Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5350321Z 182 |             logger.info(f"Memory version saved: {version_file.name}")
2026-01-26T14:33:47.5350453Z 183 |             return f"Memory version saved: {version_file.name}"
2026-01-26T14:33:47.5350515Z     |
2026-01-26T14:33:47.5350606Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5350611Z 
2026-01-26T14:33:47.5350694Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5350770Z    --> memory_manager.py:187:1
2026-01-26T14:33:47.5350835Z     |
2026-01-26T14:33:47.5350949Z 185 |             logger.error(f"Error saving version: {e}")
2026-01-26T14:33:47.5351048Z 186 |             return f"Error saving version: {e}"
2026-01-26T14:33:47.5351108Z 187 |     
2026-01-26T14:33:47.5351172Z     | ^^^^
2026-01-26T14:33:47.5351259Z 188 |     def list_versions(self) -> str:
2026-01-26T14:33:47.5351318Z 189 |         """
2026-01-26T14:33:47.5351380Z     |
2026-01-26T14:33:47.5351464Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5351469Z 
2026-01-26T14:33:47.5351547Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5351627Z    --> memory_manager.py:191:1
2026-01-26T14:33:47.5351821Z     |
2026-01-26T14:33:47.5351882Z 189 |         """
2026-01-26T14:33:47.5351974Z 190 |         Lists all saved memory versions.
2026-01-26T14:33:47.5352040Z 191 |         
2026-01-26T14:33:47.5352099Z     | ^^^^^^^^
2026-01-26T14:33:47.5352262Z 192 |         Returns:
2026-01-26T14:33:47.5352369Z 193 |             Formatted list of versions or error
2026-01-26T14:33:47.5352428Z     |
2026-01-26T14:33:47.5352512Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5352518Z 
2026-01-26T14:33:47.5352598Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5352679Z    --> memory_manager.py:197:1
2026-01-26T14:33:47.5352737Z     |
2026-01-26T14:33:47.5352830Z 195 |         if not self.history_dir.exists():
2026-01-26T14:33:47.5352930Z 196 |             return "No memory versions found"
2026-01-26T14:33:47.5352991Z 197 |         
2026-01-26T14:33:47.5353050Z     | ^^^^^^^^
2026-01-26T14:33:47.5353111Z 198 |         try:
2026-01-26T14:33:47.5353192Z 199 |             versions = []
2026-01-26T14:33:47.5353251Z     |
2026-01-26T14:33:47.5353335Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5353340Z 
2026-01-26T14:33:47.5353424Z UP015 [*] Unnecessary mode argument
2026-01-26T14:33:47.5353506Z    --> memory_manager.py:202:42
2026-01-26T14:33:47.5353565Z     |
2026-01-26T14:33:47.5353778Z 200 |             for meta_file in sorted(self.history_dir.glob("*.meta.json"), reverse=True):
2026-01-26T14:33:47.5353846Z 201 |                 try:
2026-01-26T14:33:47.5353949Z 202 |                     with open(meta_file, "r") as f:
2026-01-26T14:33:47.5354030Z     |                                          ^^^
2026-01-26T14:33:47.5354126Z 203 |                         meta = json.load(f)
2026-01-26T14:33:47.5354184Z     |
2026-01-26T14:33:47.5354259Z help: Remove mode argument
2026-01-26T14:33:47.5354264Z 
2026-01-26T14:33:47.5354348Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5354424Z    --> memory_manager.py:204:1
2026-01-26T14:33:47.5354485Z     |
2026-01-26T14:33:47.5354588Z 202 |                     with open(meta_file, "r") as f:
2026-01-26T14:33:47.5354671Z 203 |                         meta = json.load(f)
2026-01-26T14:33:47.5354735Z 204 |                     
2026-01-26T14:33:47.5354801Z     | ^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5354931Z 205 |                     timestamp = meta.get("timestamp", "unknown")
2026-01-26T14:33:47.5355048Z 206 |                     description = meta.get("description", "")
2026-01-26T14:33:47.5355106Z     |
2026-01-26T14:33:47.5355201Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5355207Z 
2026-01-26T14:33:47.5355289Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5355364Z    --> memory_manager.py:208:1
2026-01-26T14:33:47.5355428Z     |
2026-01-26T14:33:47.5355542Z 206 |                     description = meta.get("description", "")
2026-01-26T14:33:47.5355647Z 207 |                     created = meta.get("created_at", "")
2026-01-26T14:33:47.5355714Z 208 |                     
2026-01-26T14:33:47.5355786Z     | ^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5355892Z 209 |                     version_info = f"- **{timestamp}**"
2026-01-26T14:33:47.5355973Z 210 |                     if description:
2026-01-26T14:33:47.5356038Z     |
2026-01-26T14:33:47.5356126Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5356132Z 
2026-01-26T14:33:47.5356212Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5356292Z    --> memory_manager.py:214:1
2026-01-26T14:33:47.5356350Z     |
2026-01-26T14:33:47.5356424Z 212 |                     if created:
2026-01-26T14:33:47.5356523Z 213 |                         version_info += f" ({created})"
2026-01-26T14:33:47.5356593Z 214 |                     
2026-01-26T14:33:47.5356658Z     | ^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5356762Z 215 |                     versions.append(version_info)
2026-01-26T14:33:47.5356843Z 216 |                 except Exception:
2026-01-26T14:33:47.5356902Z     |
2026-01-26T14:33:47.5356986Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5357075Z 
2026-01-26T14:33:47.5357157Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5357241Z    --> memory_manager.py:218:1
2026-01-26T14:33:47.5357298Z     |
2026-01-26T14:33:47.5357443Z 216 |                 except Exception:
2026-01-26T14:33:47.5357523Z 217 |                     continue
2026-01-26T14:33:47.5357583Z 218 |             
2026-01-26T14:33:47.5357643Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5357714Z 219 |             if not versions:
2026-01-26T14:33:47.5357817Z 220 |                 return "No memory versions found"
2026-01-26T14:33:47.5357875Z     |
2026-01-26T14:33:47.5357958Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5357963Z 
2026-01-26T14:33:47.5358047Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5358126Z    --> memory_manager.py:221:1
2026-01-26T14:33:47.5358184Z     |
2026-01-26T14:33:47.5358261Z 219 |             if not versions:
2026-01-26T14:33:47.5358357Z 220 |                 return "No memory versions found"
2026-01-26T14:33:47.5358421Z 221 |             
2026-01-26T14:33:47.5358480Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5358613Z 222 |             return "# MEMORY VERSIONS\n\n" + "\n".join(versions)
2026-01-26T14:33:47.5358696Z 223 |         except Exception as e:
2026-01-26T14:33:47.5358758Z     |
2026-01-26T14:33:47.5359075Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5359089Z 
2026-01-26T14:33:47.5359191Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5359272Z    --> memory_manager.py:226:1
2026-01-26T14:33:47.5359336Z     |
2026-01-26T14:33:47.5359459Z 224 |             logger.error(f"Error listing versions: {e}")
2026-01-26T14:33:47.5359558Z 225 |             return f"Error listing versions: {e}"
2026-01-26T14:33:47.5359620Z 226 |     
2026-01-26T14:33:47.5359684Z     | ^^^^
2026-01-26T14:33:47.5359813Z 227 |     def restore_version(self, timestamp: str) -> str:
2026-01-26T14:33:47.5359875Z 228 |         """
2026-01-26T14:33:47.5359942Z     |
2026-01-26T14:33:47.5360036Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5360041Z 
2026-01-26T14:33:47.5360122Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5360197Z    --> memory_manager.py:230:1
2026-01-26T14:33:47.5360261Z     |
2026-01-26T14:33:47.5360324Z 228 |         """
2026-01-26T14:33:47.5360419Z 229 |         Restores a specific memory version.
2026-01-26T14:33:47.5360485Z 230 |         
2026-01-26T14:33:47.5360544Z     | ^^^^^^^^
2026-01-26T14:33:47.5360605Z 231 |         Args:
2026-01-26T14:33:47.5360731Z 232 |             timestamp: Timestamp of version to restore
2026-01-26T14:33:47.5360789Z     |
2026-01-26T14:33:47.5360873Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5360878Z 
2026-01-26T14:33:47.5360962Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5361038Z    --> memory_manager.py:233:1
2026-01-26T14:33:47.5361101Z     |
2026-01-26T14:33:47.5361163Z 231 |         Args:
2026-01-26T14:33:47.5361280Z 232 |             timestamp: Timestamp of version to restore
2026-01-26T14:33:47.5361343Z 233 |             
2026-01-26T14:33:47.5361402Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5361471Z 234 |         Returns:
2026-01-26T14:33:47.5361556Z 235 |             Success message or error
2026-01-26T14:33:47.5361613Z     |
2026-01-26T14:33:47.5361699Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5361710Z 
2026-01-26T14:33:47.5361790Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5361879Z    --> memory_manager.py:239:1
2026-01-26T14:33:47.5361937Z     |
2026-01-26T14:33:47.5362038Z 237 |         if not self.history_dir.exists():
2026-01-26T14:33:47.5362133Z 238 |             return "No memory versions found"
2026-01-26T14:33:47.5362193Z 239 |         
2026-01-26T14:33:47.5362258Z     | ^^^^^^^^
2026-01-26T14:33:47.5362320Z 240 |         try:
2026-01-26T14:33:47.5362484Z 241 |             version_file = self.history_dir / f"memory_{timestamp}.md"
2026-01-26T14:33:47.5362543Z     |
2026-01-26T14:33:47.5362660Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5362808Z 
2026-01-26T14:33:47.5362902Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5362983Z    --> memory_manager.py:242:1
2026-01-26T14:33:47.5363046Z     |
2026-01-26T14:33:47.5363113Z 240 |         try:
2026-01-26T14:33:47.5363369Z 241 |             version_file = self.history_dir / f"memory_{timestamp}.md"
2026-01-26T14:33:47.5363458Z 242 |             
2026-01-26T14:33:47.5363517Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5363608Z 243 |             if not version_file.exists():
2026-01-26T14:33:47.5363729Z 244 |                 return f"Version not found: {timestamp}"
2026-01-26T14:33:47.5363793Z     |
2026-01-26T14:33:47.5363882Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5363887Z 
2026-01-26T14:33:47.5363968Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5364052Z    --> memory_manager.py:245:1
2026-01-26T14:33:47.5364110Z     |
2026-01-26T14:33:47.5364201Z 243 |             if not version_file.exists():
2026-01-26T14:33:47.5364322Z 244 |                 return f"Version not found: {timestamp}"
2026-01-26T14:33:47.5364381Z 245 |             
2026-01-26T14:33:47.5364441Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5364602Z 246 |             self.save_version(description="Auto-backup before restore")
2026-01-26T14:33:47.5364668Z     |
2026-01-26T14:33:47.5364751Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5364757Z 
2026-01-26T14:33:47.5364835Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5364916Z    --> memory_manager.py:247:1
2026-01-26T14:33:47.5364974Z     |
2026-01-26T14:33:47.5365127Z 246 |             self.save_version(description="Auto-backup before restore")
2026-01-26T14:33:47.5365188Z 247 |             
2026-01-26T14:33:47.5365252Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5365369Z 248 |             shutil.copy2(version_file, self.memory_file)
2026-01-26T14:33:47.5365427Z     |
2026-01-26T14:33:47.5365519Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5365523Z 
2026-01-26T14:33:47.5365607Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5365682Z    --> memory_manager.py:249:1
2026-01-26T14:33:47.5365744Z     |
2026-01-26T14:33:47.5365859Z 248 |             shutil.copy2(version_file, self.memory_file)
2026-01-26T14:33:47.5365919Z 249 |             
2026-01-26T14:33:47.5365981Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5366140Z 250 |             logger.info(f"Memory restored from version: {timestamp}")
2026-01-26T14:33:47.5366273Z 251 |             return f"Memory restored from version: {timestamp}"
2026-01-26T14:33:47.5366330Z     |
2026-01-26T14:33:47.5366419Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5366424Z 
2026-01-26T14:33:47.5366529Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5366613Z   --> scripts/organize_docs.py:18:1
2026-01-26T14:33:47.5366675Z    |
2026-01-26T14:33:47.5366734Z 16 |   """
2026-01-26T14:33:47.5366792Z 17 |
2026-01-26T14:33:47.5366856Z 18 | / import os
2026-01-26T14:33:47.5366926Z 19 | | import sys
2026-01-26T14:33:47.5366996Z 20 | | import shutil
2026-01-26T14:33:47.5367064Z 21 | | import hashlib
2026-01-26T14:33:47.5367138Z 22 | | import argparse
2026-01-26T14:33:47.5367219Z 23 | | from pathlib import Path
2026-01-26T14:33:47.5367301Z 24 | | from datetime import datetime
2026-01-26T14:33:47.5367409Z 25 | | from typing import List, Dict, Set, Tuple
2026-01-26T14:33:47.5367508Z 26 | | from difflib import SequenceMatcher
2026-01-26T14:33:47.5367579Z    | |___________________________________^
2026-01-26T14:33:47.5367637Z    |
2026-01-26T14:33:47.5367716Z help: Organize imports
2026-01-26T14:33:47.5367721Z 
2026-01-26T14:33:47.5367799Z F401 [*] `sys` imported but unused
2026-01-26T14:33:47.5367923Z   --> scripts/organize_docs.py:19:8
2026-01-26T14:33:47.5367981Z    |
2026-01-26T14:33:47.5368050Z 18 | import os
2026-01-26T14:33:47.5368111Z 19 | import sys
2026-01-26T14:33:47.5368171Z    |        ^^^
2026-01-26T14:33:47.5368240Z 20 | import shutil
2026-01-26T14:33:47.5368303Z 21 | import hashlib
2026-01-26T14:33:47.5368446Z    |
2026-01-26T14:33:47.5368531Z help: Remove unused import: `sys`
2026-01-26T14:33:47.5368541Z 
2026-01-26T14:33:47.5368625Z F401 [*] `hashlib` imported but unused
2026-01-26T14:33:47.5368704Z   --> scripts/organize_docs.py:21:8
2026-01-26T14:33:47.5368955Z    |
2026-01-26T14:33:47.5369174Z 19 | import sys
2026-01-26T14:33:47.5369252Z 20 | import shutil
2026-01-26T14:33:47.5369317Z 21 | import hashlib
2026-01-26T14:33:47.5369382Z    |        ^^^^^^^
2026-01-26T14:33:47.5369451Z 22 | import argparse
2026-01-26T14:33:47.5369533Z 23 | from pathlib import Path
2026-01-26T14:33:47.5369592Z    |
2026-01-26T14:33:47.5369684Z help: Remove unused import: `hashlib`
2026-01-26T14:33:47.5369690Z 
2026-01-26T14:33:47.5369795Z F401 [*] `datetime.datetime` imported but unused
2026-01-26T14:33:47.5369881Z   --> scripts/organize_docs.py:24:22
2026-01-26T14:33:47.5369947Z    |
2026-01-26T14:33:47.5370013Z 22 | import argparse
2026-01-26T14:33:47.5370093Z 23 | from pathlib import Path
2026-01-26T14:33:47.5370178Z 24 | from datetime import datetime
2026-01-26T14:33:47.5370253Z    |                      ^^^^^^^^
2026-01-26T14:33:47.5370353Z 25 | from typing import List, Dict, Set, Tuple
2026-01-26T14:33:47.5370443Z 26 | from difflib import SequenceMatcher
2026-01-26T14:33:47.5370505Z    |
2026-01-26T14:33:47.5370614Z help: Remove unused import: `datetime.datetime`
2026-01-26T14:33:47.5370619Z 
2026-01-26T14:33:47.5370742Z UP035 `typing.List` is deprecated, use `list` instead
2026-01-26T14:33:47.5370834Z   --> scripts/organize_docs.py:25:1
2026-01-26T14:33:47.5370892Z    |
2026-01-26T14:33:47.5370967Z 23 | from pathlib import Path
2026-01-26T14:33:47.5371047Z 24 | from datetime import datetime
2026-01-26T14:33:47.5371152Z 25 | from typing import List, Dict, Set, Tuple
2026-01-26T14:33:47.5371225Z    | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5371316Z 26 | from difflib import SequenceMatcher
2026-01-26T14:33:47.5371378Z    |
2026-01-26T14:33:47.5371383Z 
2026-01-26T14:33:47.5371506Z UP035 `typing.Dict` is deprecated, use `dict` instead
2026-01-26T14:33:47.5371594Z   --> scripts/organize_docs.py:25:1
2026-01-26T14:33:47.5371653Z    |
2026-01-26T14:33:47.5371734Z 23 | from pathlib import Path
2026-01-26T14:33:47.5371812Z 24 | from datetime import datetime
2026-01-26T14:33:47.5371910Z 25 | from typing import List, Dict, Set, Tuple
2026-01-26T14:33:47.5371988Z    | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5372074Z 26 | from difflib import SequenceMatcher
2026-01-26T14:33:47.5372131Z    |
2026-01-26T14:33:47.5372135Z 
2026-01-26T14:33:47.5372252Z UP035 `typing.Set` is deprecated, use `set` instead
2026-01-26T14:33:47.5372335Z   --> scripts/organize_docs.py:25:1
2026-01-26T14:33:47.5372393Z    |
2026-01-26T14:33:47.5372469Z 23 | from pathlib import Path
2026-01-26T14:33:47.5372553Z 24 | from datetime import datetime
2026-01-26T14:33:47.5372644Z 25 | from typing import List, Dict, Set, Tuple
2026-01-26T14:33:47.5372717Z    | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5372808Z 26 | from difflib import SequenceMatcher
2026-01-26T14:33:47.5372872Z    |
2026-01-26T14:33:47.5372876Z 
2026-01-26T14:33:47.5373002Z UP035 `typing.Tuple` is deprecated, use `tuple` instead
2026-01-26T14:33:47.5373088Z   --> scripts/organize_docs.py:25:1
2026-01-26T14:33:47.5373148Z    |
2026-01-26T14:33:47.5373223Z 23 | from pathlib import Path
2026-01-26T14:33:47.5373299Z 24 | from datetime import datetime
2026-01-26T14:33:47.5373401Z 25 | from typing import List, Dict, Set, Tuple
2026-01-26T14:33:47.5373474Z    | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5373562Z 26 | from difflib import SequenceMatcher
2026-01-26T14:33:47.5373628Z    |
2026-01-26T14:33:47.5373633Z 
2026-01-26T14:33:47.5373722Z F401 [*] `typing.Dict` imported but unused
2026-01-26T14:33:47.5373807Z   --> scripts/organize_docs.py:25:26
2026-01-26T14:33:47.5373865Z    |
2026-01-26T14:33:47.5373946Z 23 | from pathlib import Path
2026-01-26T14:33:47.5374023Z 24 | from datetime import datetime
2026-01-26T14:33:47.5374115Z 25 | from typing import List, Dict, Set, Tuple
2026-01-26T14:33:47.5374313Z    |                          ^^^^
2026-01-26T14:33:47.5374399Z 26 | from difflib import SequenceMatcher
2026-01-26T14:33:47.5374459Z    |
2026-01-26T14:33:47.5374540Z help: Remove unused import
2026-01-26T14:33:47.5374614Z 
2026-01-26T14:33:47.5374703Z F401 [*] `typing.Set` imported but unused
2026-01-26T14:33:47.5374785Z   --> scripts/organize_docs.py:25:32
2026-01-26T14:33:47.5374843Z    |
2026-01-26T14:33:47.5374922Z 23 | from pathlib import Path
2026-01-26T14:33:47.5375000Z 24 | from datetime import datetime
2026-01-26T14:33:47.5375100Z 25 | from typing import List, Dict, Set, Tuple
2026-01-26T14:33:47.5375174Z    |                                ^^^
2026-01-26T14:33:47.5375260Z 26 | from difflib import SequenceMatcher
2026-01-26T14:33:47.5375318Z    |
2026-01-26T14:33:47.5375393Z help: Remove unused import
2026-01-26T14:33:47.5375404Z 
2026-01-26T14:33:47.5375486Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5375566Z   --> scripts/organize_docs.py:34:1
2026-01-26T14:33:47.5375627Z    |
2026-01-26T14:33:47.5375706Z 32 |         self.dry_run = dry_run
2026-01-26T14:33:47.5375779Z 33 |         self.verbose = verbose
2026-01-26T14:33:47.5375840Z 34 |         
2026-01-26T14:33:47.5375909Z    | ^^^^^^^^
2026-01-26T14:33:47.5376000Z 35 |         self.docs_dir = root_dir / "docs"
2026-01-26T14:33:47.5376118Z 36 |         self.archive_dir = self.docs_dir / "archive"
2026-01-26T14:33:47.5376177Z    |
2026-01-26T14:33:47.5376273Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5376278Z 
2026-01-26T14:33:47.5376360Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5376446Z   --> scripts/organize_docs.py:37:1
2026-01-26T14:33:47.5376511Z    |
2026-01-26T14:33:47.5376605Z 35 |         self.docs_dir = root_dir / "docs"
2026-01-26T14:33:47.5376721Z 36 |         self.archive_dir = self.docs_dir / "archive"
2026-01-26T14:33:47.5376785Z 37 |         
2026-01-26T14:33:47.5376845Z    | ^^^^^^^^
2026-01-26T14:33:47.5376922Z 38 |         # Files to keep in root
2026-01-26T14:33:47.5377001Z 39 |         self.root_whitelist = {
2026-01-26T14:33:47.5377065Z    |
2026-01-26T14:33:47.5377153Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5377158Z 
2026-01-26T14:33:47.5377241Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5377330Z   --> scripts/organize_docs.py:47:1
2026-01-26T14:33:47.5377388Z    |
2026-01-26T14:33:47.5377467Z 45 |             "CODE_OF_CONDUCT.md",
2026-01-26T14:33:47.5377527Z 46 |         }
2026-01-26T14:33:47.5377591Z 47 |         
2026-01-26T14:33:47.5377648Z    | ^^^^^^^^
2026-01-26T14:33:47.5377721Z 48 |         # Directories to ignore
2026-01-26T14:33:47.5377801Z 49 |         self.ignore_dirs = {
2026-01-26T14:33:47.5377859Z    |
2026-01-26T14:33:47.5377948Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5377952Z 
2026-01-26T14:33:47.5378032Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5378121Z   --> scripts/organize_docs.py:61:1
2026-01-26T14:33:47.5378183Z    |
2026-01-26T14:33:47.5378252Z 59 |             "build",
2026-01-26T14:33:47.5378317Z 60 |         }
2026-01-26T14:33:47.5378375Z 61 |         
2026-01-26T14:33:47.5378432Z    | ^^^^^^^^
2026-01-26T14:33:47.5378522Z 62 |         self.changes: List[str] = []
2026-01-26T14:33:47.5378595Z 63 |         self.stats = {
2026-01-26T14:33:47.5378654Z    |
2026-01-26T14:33:47.5378737Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5378742Z 
2026-01-26T14:33:47.5378986Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5379071Z   --> scripts/organize_docs.py:62:23
2026-01-26T14:33:47.5379127Z    |
2026-01-26T14:33:47.5379190Z 60 |         }
2026-01-26T14:33:47.5379249Z 61 |         
2026-01-26T14:33:47.5379332Z 62 |         self.changes: List[str] = []
2026-01-26T14:33:47.5379400Z    |                       ^^^^
2026-01-26T14:33:47.5379473Z 63 |         self.stats = {
2026-01-26T14:33:47.5379542Z 64 |             "moved": 0,
2026-01-26T14:33:47.5379600Z    |
2026-01-26T14:33:47.5379805Z help: Replace with `list`
2026-01-26T14:33:47.5379811Z 
2026-01-26T14:33:47.5379892Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5379972Z   --> scripts/organize_docs.py:69:1
2026-01-26T14:33:47.5380030Z    |
2026-01-26T14:33:47.5380253Z 67 |             "deleted": 0,
2026-01-26T14:33:47.5380316Z 68 |         }
2026-01-26T14:33:47.5380375Z 69 |     
2026-01-26T14:33:47.5380437Z    | ^^^^
2026-01-26T14:33:47.5380558Z 70 |     def log(self, message: str, level: str = "INFO"):
2026-01-26T14:33:47.5380630Z 71 |         """Log message"""
2026-01-26T14:33:47.5380692Z    |
2026-01-26T14:33:47.5380781Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5380787Z 
2026-01-26T14:33:47.5380867Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5380953Z   --> scripts/organize_docs.py:77:1
2026-01-26T14:33:47.5381015Z    |
2026-01-26T14:33:47.5381085Z 75 |         elif level == "ERROR":
2026-01-26T14:33:47.5381373Z 76 |             prefix = "❌"
2026-01-26T14:33:47.5381438Z 77 |         
2026-01-26T14:33:47.5381505Z    | ^^^^^^^^
2026-01-26T14:33:47.5381625Z 78 |         if self.verbose or level in ["WARN", "ERROR"]:
2026-01-26T14:33:47.5381720Z 79 |             print(f"{prefix} {message}")
2026-01-26T14:33:47.5381786Z    |
2026-01-26T14:33:47.5381880Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5381885Z 
2026-01-26T14:33:47.5381969Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5382056Z   --> scripts/organize_docs.py:80:1
2026-01-26T14:33:47.5382114Z    |
2026-01-26T14:33:47.5382227Z 78 |         if self.verbose or level in ["WARN", "ERROR"]:
2026-01-26T14:33:47.5382319Z 79 |             print(f"{prefix} {message}")
2026-01-26T14:33:47.5382377Z 80 |     
2026-01-26T14:33:47.5382436Z    | ^^^^
2026-01-26T14:33:47.5382549Z 81 |     def find_markdown_files(self) -> List[Path]:
2026-01-26T14:33:47.5382651Z 82 |         """Find all markdown files in project"""
2026-01-26T14:33:47.5382709Z    |
2026-01-26T14:33:47.5382795Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5382805Z 
2026-01-26T14:33:47.5382934Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5383018Z   --> scripts/organize_docs.py:81:38
2026-01-26T14:33:47.5383075Z    |
2026-01-26T14:33:47.5383162Z 79 |             print(f"{prefix} {message}")
2026-01-26T14:33:47.5383226Z 80 |     
2026-01-26T14:33:47.5383327Z 81 |     def find_markdown_files(self) -> List[Path]:
2026-01-26T14:33:47.5383404Z    |                                      ^^^^
2026-01-26T14:33:47.5383502Z 82 |         """Find all markdown files in project"""
2026-01-26T14:33:47.5383572Z 83 |         md_files = []
2026-01-26T14:33:47.5383630Z    |
2026-01-26T14:33:47.5383708Z help: Replace with `list`
2026-01-26T14:33:47.5383714Z 
2026-01-26T14:33:47.5383796Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5383875Z   --> scripts/organize_docs.py:84:1
2026-01-26T14:33:47.5383932Z    |
2026-01-26T14:33:47.5384031Z 82 |         """Find all markdown files in project"""
2026-01-26T14:33:47.5384103Z 83 |         md_files = []
2026-01-26T14:33:47.5384162Z 84 |         
2026-01-26T14:33:47.5384225Z    | ^^^^^^^^
2026-01-26T14:33:47.5384344Z 85 |         for root, dirs, files in os.walk(self.root_dir):
2026-01-26T14:33:47.5384432Z 86 |             # Skip ignored directories
2026-01-26T14:33:47.5384489Z    |
2026-01-26T14:33:47.5384579Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5384584Z 
2026-01-26T14:33:47.5385220Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5385308Z   --> scripts/organize_docs.py:88:1
2026-01-26T14:33:47.5385372Z    |
2026-01-26T14:33:47.5385455Z 86 |             # Skip ignored directories
2026-01-26T14:33:47.5385593Z 87 |             dirs[:] = [d for d in dirs if d not in self.ignore_dirs]
2026-01-26T14:33:47.5385658Z 88 |             
2026-01-26T14:33:47.5385717Z    | ^^^^^^^^^^^^
2026-01-26T14:33:47.5385789Z 89 |             for file in files:
2026-01-26T14:33:47.5385878Z 90 |                 if file.endswith(".md"):
2026-01-26T14:33:47.5386026Z    |
2026-01-26T14:33:47.5386114Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5386120Z 
2026-01-26T14:33:47.5386201Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5386287Z   --> scripts/organize_docs.py:92:1
2026-01-26T14:33:47.5386345Z    |
2026-01-26T14:33:47.5386503Z 90 |                 if file.endswith(".md"):
2026-01-26T14:33:47.5386616Z 91 |                     md_files.append(Path(root) / file)
2026-01-26T14:33:47.5386676Z 92 |         
2026-01-26T14:33:47.5386733Z    | ^^^^^^^^
2026-01-26T14:33:47.5386807Z 93 |         return md_files
2026-01-26T14:33:47.5386869Z    |
2026-01-26T14:33:47.5386956Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5386961Z 
2026-01-26T14:33:47.5387042Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5387127Z   --> scripts/organize_docs.py:94:1
2026-01-26T14:33:47.5387184Z    |
2026-01-26T14:33:47.5387254Z 93 |         return md_files
2026-01-26T14:33:47.5387317Z 94 |     
2026-01-26T14:33:47.5387376Z    | ^^^^
2026-01-26T14:33:47.5387508Z 95 |     def is_versioned_file(self, filename: str) -> bool:
2026-01-26T14:33:47.5387616Z 96 |         """Check if filename indicates versioning"""
2026-01-26T14:33:47.5387679Z    |
2026-01-26T14:33:47.5387766Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5387771Z 
2026-01-26T14:33:47.5387851Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5387940Z    --> scripts/organize_docs.py:99:1
2026-01-26T14:33:47.5387999Z     |
2026-01-26T14:33:47.5388191Z  97 |         version_patterns = ["_v0.", "_v1.", "_v2.", "-v0.", "-v1.", "-v2.", "version"]
2026-01-26T14:33:47.5388386Z  98 |         return any(pattern in filename.lower() for pattern in version_patterns)
2026-01-26T14:33:47.5388450Z  99 |     
2026-01-26T14:33:47.5388509Z     | ^^^^
2026-01-26T14:33:47.5388634Z 100 |     def is_date_file(self, filename: str) -> bool:
2026-01-26T14:33:47.5388738Z 101 |         """Check if filename contains date"""
2026-01-26T14:33:47.5388905Z     |
2026-01-26T14:33:47.5389000Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5389005Z 
2026-01-26T14:33:47.5389089Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5389175Z    --> scripts/organize_docs.py:105:1
2026-01-26T14:33:47.5389232Z     |
2026-01-26T14:33:47.5389352Z 103 |         date_pattern = r"\d{4}[-_]\d{2}[-_]\d{2}"
2026-01-26T14:33:47.5389476Z 104 |         return bool(re.search(date_pattern, filename))
2026-01-26T14:33:47.5389534Z 105 |     
2026-01-26T14:33:47.5389592Z     | ^^^^
2026-01-26T14:33:47.5389772Z 106 |     def calculate_similarity(self, file1: Path, file2: Path) -> float:
2026-01-26T14:33:47.5389882Z 107 |         """Calculate similarity between two files"""
2026-01-26T14:33:47.5389942Z     |
2026-01-26T14:33:47.5390032Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5390037Z 
2026-01-26T14:33:47.5390117Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5390200Z    --> scripts/organize_docs.py:111:1
2026-01-26T14:33:47.5390258Z     |
2026-01-26T14:33:47.5390428Z 109 |             content1 = file1.read_text(encoding="utf-8", errors="ignore")
2026-01-26T14:33:47.5390579Z 110 |             content2 = file2.read_text(encoding="utf-8", errors="ignore")
2026-01-26T14:33:47.5390640Z 111 |             
2026-01-26T14:33:47.5390707Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5390857Z 112 |             return SequenceMatcher(None, content1, content2).ratio()
2026-01-26T14:33:47.5390934Z 113 |         except Exception:
2026-01-26T14:33:47.5390998Z     |
2026-01-26T14:33:47.5391082Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5391087Z 
2026-01-26T14:33:47.5391166Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5391248Z    --> scripts/organize_docs.py:115:1
2026-01-26T14:33:47.5391311Z     |
2026-01-26T14:33:47.5391383Z 113 |         except Exception:
2026-01-26T14:33:47.5391451Z 114 |             return 0.0
2026-01-26T14:33:47.5391514Z 115 |     
2026-01-26T14:33:47.5391573Z     | ^^^^
2026-01-26T14:33:47.5391798Z 116 |     def find_duplicates(self, md_files: List[Path]) -> List[Tuple[Path, Path, float]]:
2026-01-26T14:33:47.5392052Z 117 |         """Find duplicate/similar documentation files"""
2026-01-26T14:33:47.5392117Z     |
2026-01-26T14:33:47.5392200Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5392309Z 
2026-01-26T14:33:47.5392436Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5392531Z    --> scripts/organize_docs.py:116:41
2026-01-26T14:33:47.5392588Z     |
2026-01-26T14:33:47.5392655Z 114 |             return 0.0
2026-01-26T14:33:47.5392718Z 115 |     
2026-01-26T14:33:47.5392928Z 116 |     def find_duplicates(self, md_files: List[Path]) -> List[Tuple[Path, Path, float]]:
2026-01-26T14:33:47.5393011Z     |                                         ^^^^
2026-01-26T14:33:47.5393134Z 117 |         """Find duplicate/similar documentation files"""
2026-01-26T14:33:47.5393215Z 118 |         duplicates = []
2026-01-26T14:33:47.5393273Z     |
2026-01-26T14:33:47.5393348Z help: Replace with `list`
2026-01-26T14:33:47.5393356Z 
2026-01-26T14:33:47.5393482Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5393566Z    --> scripts/organize_docs.py:116:56
2026-01-26T14:33:47.5393624Z     |
2026-01-26T14:33:47.5393695Z 114 |             return 0.0
2026-01-26T14:33:47.5393757Z 115 |     
2026-01-26T14:33:47.5393964Z 116 |     def find_duplicates(self, md_files: List[Path]) -> List[Tuple[Path, Path, float]]:
2026-01-26T14:33:47.5394060Z     |                                                        ^^^^
2026-01-26T14:33:47.5394183Z 117 |         """Find duplicate/similar documentation files"""
2026-01-26T14:33:47.5394254Z 118 |         duplicates = []
2026-01-26T14:33:47.5394312Z     |
2026-01-26T14:33:47.5394391Z help: Replace with `list`
2026-01-26T14:33:47.5394396Z 
2026-01-26T14:33:47.5394522Z UP006 [*] Use `tuple` instead of `Tuple` for type annotation
2026-01-26T14:33:47.5394608Z    --> scripts/organize_docs.py:116:61
2026-01-26T14:33:47.5394672Z     |
2026-01-26T14:33:47.5394738Z 114 |             return 0.0
2026-01-26T14:33:47.5394801Z 115 |     
2026-01-26T14:33:47.5395009Z 116 |     def find_duplicates(self, md_files: List[Path]) -> List[Tuple[Path, Path, float]]:
2026-01-26T14:33:47.5395118Z     |                                                             ^^^^^
2026-01-26T14:33:47.5395237Z 117 |         """Find duplicate/similar documentation files"""
2026-01-26T14:33:47.5395308Z 118 |         duplicates = []
2026-01-26T14:33:47.5395369Z     |
2026-01-26T14:33:47.5395444Z help: Replace with `tuple`
2026-01-26T14:33:47.5395450Z 
2026-01-26T14:33:47.5395530Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5395618Z    --> scripts/organize_docs.py:119:1
2026-01-26T14:33:47.5395677Z     |
2026-01-26T14:33:47.5395794Z 117 |         """Find duplicate/similar documentation files"""
2026-01-26T14:33:47.5395865Z 118 |         duplicates = []
2026-01-26T14:33:47.5395930Z 119 |         
2026-01-26T14:33:47.5395989Z     | ^^^^^^^^
2026-01-26T14:33:47.5396083Z 120 |         for i, file1 in enumerate(md_files):
2026-01-26T14:33:47.5396183Z 121 |             for file2 in md_files[i + 1:]:
2026-01-26T14:33:47.5396245Z     |
2026-01-26T14:33:47.5396332Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5396337Z 
2026-01-26T14:33:47.5396420Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5396507Z    --> scripts/organize_docs.py:123:1
2026-01-26T14:33:47.5396565Z     |
2026-01-26T14:33:47.5396654Z 121 |             for file2 in md_files[i + 1:]:
2026-01-26T14:33:47.5396799Z 122 |                 similarity = self.calculate_similarity(file1, file2)
2026-01-26T14:33:47.5396862Z 123 |                 
2026-01-26T14:33:47.5396925Z     | ^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5397029Z 124 |                 if similarity > 0.85:  # 85% similar
2026-01-26T14:33:47.5397159Z 125 |                     duplicates.append((file1, file2, similarity))
2026-01-26T14:33:47.5397218Z     |
2026-01-26T14:33:47.5397303Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5397308Z 
2026-01-26T14:33:47.5397496Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5397588Z    --> scripts/organize_docs.py:126:1
2026-01-26T14:33:47.5397646Z     |
2026-01-26T14:33:47.5397747Z 124 |                 if similarity > 0.85:  # 85% similar
2026-01-26T14:33:47.5397942Z 125 |                     duplicates.append((file1, file2, similarity))
2026-01-26T14:33:47.5398005Z 126 |         
2026-01-26T14:33:47.5398070Z     | ^^^^^^^^
2026-01-26T14:33:47.5398144Z 127 |         return duplicates
2026-01-26T14:33:47.5398206Z     |
2026-01-26T14:33:47.5398291Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5398295Z 
2026-01-26T14:33:47.5398380Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5398463Z    --> scripts/organize_docs.py:128:1
2026-01-26T14:33:47.5398525Z     |
2026-01-26T14:33:47.5398601Z 127 |         return duplicates
2026-01-26T14:33:47.5398667Z 128 |     
2026-01-26T14:33:47.5398725Z     | ^^^^
2026-01-26T14:33:47.5398954Z 129 |     def organize_root_files(self, md_files: List[Path]):
2026-01-26T14:33:47.5399127Z 130 |         """Move non-whitelisted .md files from root to docs/"""
2026-01-26T14:33:47.5399186Z     |
2026-01-26T14:33:47.5399270Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5399275Z 
2026-01-26T14:33:47.5399399Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5399483Z    --> scripts/organize_docs.py:129:45
2026-01-26T14:33:47.5399541Z     |
2026-01-26T14:33:47.5399624Z 127 |         return duplicates
2026-01-26T14:33:47.5399683Z 128 |     
2026-01-26T14:33:47.5399808Z 129 |     def organize_root_files(self, md_files: List[Path]):
2026-01-26T14:33:47.5399894Z     |                                             ^^^^
2026-01-26T14:33:47.5400031Z 130 |         """Move non-whitelisted .md files from root to docs/"""
2026-01-26T14:33:47.5400107Z 131 |         for md_file in md_files:
2026-01-26T14:33:47.5400167Z     |
2026-01-26T14:33:47.5400248Z help: Replace with `list`
2026-01-26T14:33:47.5400253Z 
2026-01-26T14:33:47.5400338Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5400420Z    --> scripts/organize_docs.py:135:1
2026-01-26T14:33:47.5400481Z     |
2026-01-26T14:33:47.5400582Z 133 |             if md_file.parent != self.root_dir:
2026-01-26T14:33:47.5400655Z 134 |                 continue
2026-01-26T14:33:47.5400717Z 135 |             
2026-01-26T14:33:47.5400782Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5400897Z 136 |             if md_file.name not in self.root_whitelist:
2026-01-26T14:33:47.5401018Z 137 |                 # Determine target directory
2026-01-26T14:33:47.5401081Z     |
2026-01-26T14:33:47.5401167Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5401172Z 
2026-01-26T14:33:47.5401252Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5401338Z    --> scripts/organize_docs.py:144:1
2026-01-26T14:33:47.5401400Z     |
2026-01-26T14:33:47.5401508Z 142 |                     target_dir = self.docs_dir / "guides"
2026-01-26T14:33:47.5401588Z 143 |                     action = "moved"
2026-01-26T14:33:47.5401659Z 144 |                 
2026-01-26T14:33:47.5401722Z     | ^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5401829Z 145 |                 target_path = target_dir / md_file.name
2026-01-26T14:33:47.5401895Z     |
2026-01-26T14:33:47.5401981Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5401986Z 
2026-01-26T14:33:47.5402066Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5402148Z    --> scripts/organize_docs.py:146:1
2026-01-26T14:33:47.5402213Z     |
2026-01-26T14:33:47.5402316Z 145 |                 target_path = target_dir / md_file.name
2026-01-26T14:33:47.5402378Z 146 |                 
2026-01-26T14:33:47.5402445Z     | ^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5402841Z 147 |                 self.log(f"{action.capitalize()}: {md_file.name} → {target_path.relative_to(self.root_dir)}")
2026-01-26T14:33:47.5402900Z     |
2026-01-26T14:33:47.5402996Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5403001Z 
2026-01-26T14:33:47.5403081Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5403294Z    --> scripts/organize_docs.py:148:1
2026-01-26T14:33:47.5403352Z     |
2026-01-26T14:33:47.5403709Z 147 |                 self.log(f"{action.capitalize()}: {md_file.name} → {target_path.relative_to(self.root_dir)}")
2026-01-26T14:33:47.5403876Z 148 |                 
2026-01-26T14:33:47.5403942Z     | ^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5404030Z 149 |                 if not self.dry_run:
2026-01-26T14:33:47.5404160Z 150 |                     target_dir.mkdir(parents=True, exist_ok=True)
2026-01-26T14:33:47.5404218Z     |
2026-01-26T14:33:47.5404307Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5404312Z 
2026-01-26T14:33:47.5404393Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5404475Z    --> scripts/organize_docs.py:152:1
2026-01-26T14:33:47.5404533Z     |
2026-01-26T14:33:47.5404658Z 150 |                     target_dir.mkdir(parents=True, exist_ok=True)
2026-01-26T14:33:47.5404776Z 151 |                     shutil.move(str(md_file), str(target_path))
2026-01-26T14:33:47.5404845Z 152 |                 
2026-01-26T14:33:47.5404911Z     | ^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5405236Z 153 |                 self.changes.append(f"- {action.capitalize()} `{md_file.name}` to `{target_path.relative_to(self.root_dir)}`")
2026-01-26T14:33:47.5405328Z 154 |                 self.stats[action] += 1
2026-01-26T14:33:47.5405394Z     |
2026-01-26T14:33:47.5405478Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5405482Z 
2026-01-26T14:33:47.5405562Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5405647Z    --> scripts/organize_docs.py:155:1
2026-01-26T14:33:47.5405704Z     |
2026-01-26T14:33:47.5406012Z 153 |                 self.changes.append(f"- {action.capitalize()} `{md_file.name}` to `{target_path.relative_to(self.root_dir)}`")
2026-01-26T14:33:47.5406098Z 154 |                 self.stats[action] += 1
2026-01-26T14:33:47.5406162Z 155 |     
2026-01-26T14:33:47.5406220Z     | ^^^^
2026-01-26T14:33:47.5406365Z 156 |     def archive_versioned_files(self, md_files: List[Path]):
2026-01-26T14:33:47.5406475Z 157 |         """Move versioned files to archive/"""
2026-01-26T14:33:47.5406534Z     |
2026-01-26T14:33:47.5406619Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5406626Z 
2026-01-26T14:33:47.5406755Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5406838Z    --> scripts/organize_docs.py:156:49
2026-01-26T14:33:47.5406897Z     |
2026-01-26T14:33:47.5406981Z 154 |                 self.stats[action] += 1
2026-01-26T14:33:47.5407045Z 155 |     
2026-01-26T14:33:47.5407182Z 156 |     def archive_versioned_files(self, md_files: List[Path]):
2026-01-26T14:33:47.5407268Z     |                                                 ^^^^
2026-01-26T14:33:47.5407370Z 157 |         """Move versioned files to archive/"""
2026-01-26T14:33:47.5407447Z 158 |         for md_file in md_files:
2026-01-26T14:33:47.5407506Z     |
2026-01-26T14:33:47.5407580Z help: Replace with `list`
2026-01-26T14:33:47.5407588Z 
2026-01-26T14:33:47.5407674Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5407758Z    --> scripts/organize_docs.py:162:1
2026-01-26T14:33:47.5407825Z     |
2026-01-26T14:33:47.5407942Z 160 |             if self.archive_dir in md_file.parents:
2026-01-26T14:33:47.5408014Z 161 |                 continue
2026-01-26T14:33:47.5408075Z 162 |             
2026-01-26T14:33:47.5408139Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5408249Z 163 |             # Skip root whitelisted files
2026-01-26T14:33:47.5408356Z 164 |             if md_file.name in self.root_whitelist:
2026-01-26T14:33:47.5408415Z     |
2026-01-26T14:33:47.5408505Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5408510Z 
2026-01-26T14:33:47.5408595Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5408678Z    --> scripts/organize_docs.py:166:1
2026-01-26T14:33:47.5408748Z     |
2026-01-26T14:33:47.5408988Z 164 |             if md_file.name in self.root_whitelist:
2026-01-26T14:33:47.5409058Z 165 |                 continue
2026-01-26T14:33:47.5409244Z 166 |             
2026-01-26T14:33:47.5409310Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5409519Z 167 |             if self.is_versioned_file(md_file.name) or self.is_date_file(md_file.name):
2026-01-26T14:33:47.5409784Z 168 |                 target_path = self.archive_dir / md_file.name
2026-01-26T14:33:47.5409854Z     |
2026-01-26T14:33:47.5409941Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5409946Z 
2026-01-26T14:33:47.5410027Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5410115Z    --> scripts/organize_docs.py:169:1
2026-01-26T14:33:47.5410175Z     |
2026-01-26T14:33:47.5410370Z 167 |             if self.is_versioned_file(md_file.name) or self.is_date_file(md_file.name):
2026-01-26T14:33:47.5410493Z 168 |                 target_path = self.archive_dir / md_file.name
2026-01-26T14:33:47.5410560Z 169 |                 
2026-01-26T14:33:47.5410622Z     | ^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5411016Z 170 |                 self.log(f"Archive: {md_file.relative_to(self.root_dir)} → {target_path.relative_to(self.root_dir)}")
2026-01-26T14:33:47.5411084Z     |
2026-01-26T14:33:47.5411168Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5411174Z 
2026-01-26T14:33:47.5411259Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5411345Z    --> scripts/organize_docs.py:171:1
2026-01-26T14:33:47.5411403Z     |
2026-01-26T14:33:47.5411759Z 170 |                 self.log(f"Archive: {md_file.relative_to(self.root_dir)} → {target_path.relative_to(self.root_dir)}")
2026-01-26T14:33:47.5411827Z 171 |                 
2026-01-26T14:33:47.5411889Z     | ^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5411969Z 172 |                 if not self.dry_run:
2026-01-26T14:33:47.5412119Z 173 |                     self.archive_dir.mkdir(parents=True, exist_ok=True)
2026-01-26T14:33:47.5412181Z     |
2026-01-26T14:33:47.5412267Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5412271Z 
2026-01-26T14:33:47.5412351Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5412448Z    --> scripts/organize_docs.py:175:1
2026-01-26T14:33:47.5412506Z     |
2026-01-26T14:33:47.5412645Z 173 |                     self.archive_dir.mkdir(parents=True, exist_ok=True)
2026-01-26T14:33:47.5412777Z 174 |                     shutil.move(str(md_file), str(target_path))
2026-01-26T14:33:47.5412841Z 175 |                 
2026-01-26T14:33:47.5412903Z     | ^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5413153Z 176 |                 self.changes.append(f"- Archived `{md_file.relative_to(self.root_dir)}` to archive")
2026-01-26T14:33:47.5413254Z 177 |                 self.stats["archived"] += 1
2026-01-26T14:33:47.5413311Z     |
2026-01-26T14:33:47.5413396Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5413400Z 
2026-01-26T14:33:47.5413485Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5413567Z    --> scripts/organize_docs.py:178:1
2026-01-26T14:33:47.5413626Z     |
2026-01-26T14:33:47.5413865Z 176 |                 self.changes.append(f"- Archived `{md_file.relative_to(self.root_dir)}` to archive")
2026-01-26T14:33:47.5413961Z 177 |                 self.stats["archived"] += 1
2026-01-26T14:33:47.5414019Z 178 |     
2026-01-26T14:33:47.5414076Z     | ^^^^
2026-01-26T14:33:47.5414211Z 179 |     def check_duplicates(self, md_files: List[Path]):
2026-01-26T14:33:47.5414297Z 180 |         """Report duplicate files"""
2026-01-26T14:33:47.5414355Z     |
2026-01-26T14:33:47.5414445Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5414450Z 
2026-01-26T14:33:47.5414574Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5414660Z    --> scripts/organize_docs.py:179:42
2026-01-26T14:33:47.5414724Z     |
2026-01-26T14:33:47.5414814Z 177 |                 self.stats["archived"] += 1
2026-01-26T14:33:47.5414874Z 178 |     
2026-01-26T14:33:47.5414992Z 179 |     def check_duplicates(self, md_files: List[Path]):
2026-01-26T14:33:47.5415080Z     |                                          ^^^^
2026-01-26T14:33:47.5415163Z 180 |         """Report duplicate files"""
2026-01-26T14:33:47.5415384Z 181 |         self.log("Checking for duplicates...", "INFO")
2026-01-26T14:33:47.5415453Z     |
2026-01-26T14:33:47.5415528Z help: Replace with `list`
2026-01-26T14:33:47.5415533Z 
2026-01-26T14:33:47.5415687Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5415777Z    --> scripts/organize_docs.py:183:1
2026-01-26T14:33:47.5415836Z     |
2026-01-26T14:33:47.5415951Z 181 |         self.log("Checking for duplicates...", "INFO")
2026-01-26T14:33:47.5416062Z 182 |         duplicates = self.find_duplicates(md_files)
2026-01-26T14:33:47.5416126Z 183 |         
2026-01-26T14:33:47.5416186Z     | ^^^^^^^^
2026-01-26T14:33:47.5416261Z 184 |         if duplicates:
2026-01-26T14:33:47.5416445Z 185 |             self.log(f"Found {len(duplicates)} potential duplicates:", "WARN")
2026-01-26T14:33:47.5416504Z     |
2026-01-26T14:33:47.5416589Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5416594Z 
2026-01-26T14:33:47.5416674Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5416766Z    --> scripts/organize_docs.py:186:1
2026-01-26T14:33:47.5416824Z     |
2026-01-26T14:33:47.5416895Z 184 |         if duplicates:
2026-01-26T14:33:47.5417068Z 185 |             self.log(f"Found {len(duplicates)} potential duplicates:", "WARN")
2026-01-26T14:33:47.5417131Z 186 |             
2026-01-26T14:33:47.5417191Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5417312Z 187 |             for file1, file2, similarity in duplicates:
2026-01-26T14:33:47.5417595Z 188 |                 self.log(f"  {file1.name} ≈ {file2.name} ({similarity:.1%} similar)", "WARN")
2026-01-26T14:33:47.5417655Z     |
2026-01-26T14:33:47.5417739Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5417749Z 
2026-01-26T14:33:47.5417831Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5417912Z    --> scripts/organize_docs.py:190:1
2026-01-26T14:33:47.5417970Z     |
2026-01-26T14:33:47.5418235Z 188 |                 self.log(f"  {file1.name} ≈ {file2.name} ({similarity:.1%} similar)", "WARN")
2026-01-26T14:33:47.5418346Z 189 |                 self.stats["duplicates_found"] += 1
2026-01-26T14:33:47.5418408Z 190 |             
2026-01-26T14:33:47.5418471Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5418757Z 191 |             self.changes.append(f"\n**⚠️ Duplicates Found:** {len(duplicates)} pairs")
2026-01-26T14:33:47.5418986Z 192 |             for file1, file2, similarity in duplicates:
2026-01-26T14:33:47.5419044Z     |
2026-01-26T14:33:47.5419135Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5419141Z 
2026-01-26T14:33:47.5419223Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5419306Z    --> scripts/organize_docs.py:196:1
2026-01-26T14:33:47.5419370Z     |
2026-01-26T14:33:47.5419432Z 194 |         else:
2026-01-26T14:33:47.5419538Z 195 |             self.log("No duplicates found", "INFO")
2026-01-26T14:33:47.5419601Z 196 |     
2026-01-26T14:33:47.5419659Z     | ^^^^
2026-01-26T14:33:47.5419782Z 197 |     def delete_empty_files(self, md_files: List[Path]):
2026-01-26T14:33:47.5419913Z 198 |         """Delete empty or nearly empty markdown files"""
2026-01-26T14:33:47.5419977Z     |
2026-01-26T14:33:47.5420061Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5420065Z 
2026-01-26T14:33:47.5420189Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5420281Z    --> scripts/organize_docs.py:197:44
2026-01-26T14:33:47.5420340Z     |
2026-01-26T14:33:47.5420441Z 195 |             self.log("No duplicates found", "INFO")
2026-01-26T14:33:47.5420503Z 196 |     
2026-01-26T14:33:47.5420623Z 197 |     def delete_empty_files(self, md_files: List[Path]):
2026-01-26T14:33:47.5420705Z     |                                            ^^^^
2026-01-26T14:33:47.5420824Z 198 |         """Delete empty or nearly empty markdown files"""
2026-01-26T14:33:47.5420909Z 199 |         for md_file in md_files:
2026-01-26T14:33:47.5420966Z     |
2026-01-26T14:33:47.5421040Z help: Replace with `list`
2026-01-26T14:33:47.5421045Z 
2026-01-26T14:33:47.5421254Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5421338Z    --> scripts/organize_docs.py:203:1
2026-01-26T14:33:47.5421396Z     |
2026-01-26T14:33:47.5421504Z 201 |             if md_file.name in self.root_whitelist:
2026-01-26T14:33:47.5421674Z 202 |                 continue
2026-01-26T14:33:47.5421737Z 203 |             
2026-01-26T14:33:47.5421797Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5421865Z 204 |             try:
2026-01-26T14:33:47.5422005Z 205 |                 content = md_file.read_text(encoding="utf-8").strip()
2026-01-26T14:33:47.5422064Z     |
2026-01-26T14:33:47.5422155Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5422161Z 
2026-01-26T14:33:47.5422244Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5422326Z    --> scripts/organize_docs.py:206:1
2026-01-26T14:33:47.5422383Z     |
2026-01-26T14:33:47.5422452Z 204 |             try:
2026-01-26T14:33:47.5422586Z 205 |                 content = md_file.read_text(encoding="utf-8").strip()
2026-01-26T14:33:47.5422654Z 206 |                 
2026-01-26T14:33:47.5422725Z     | ^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5422836Z 207 |                 # Consider file empty if < 50 characters
2026-01-26T14:33:47.5422918Z 208 |                 if len(content) < 50:
2026-01-26T14:33:47.5422984Z     |
2026-01-26T14:33:47.5423069Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5423074Z 
2026-01-26T14:33:47.5423156Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5423236Z    --> scripts/organize_docs.py:210:1
2026-01-26T14:33:47.5423298Z     |
2026-01-26T14:33:47.5423378Z 208 |                 if len(content) < 50:
2026-01-26T14:33:47.5423575Z 209 |                     self.log(f"Delete empty: {md_file.relative_to(self.root_dir)}", "WARN")
2026-01-26T14:33:47.5423645Z 210 |                     
2026-01-26T14:33:47.5423710Z     | ^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5423798Z 211 |                     if not self.dry_run:
2026-01-26T14:33:47.5423887Z 212 |                         md_file.unlink()
2026-01-26T14:33:47.5423949Z     |
2026-01-26T14:33:47.5424034Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5424038Z 
2026-01-26T14:33:47.5424119Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5424208Z    --> scripts/organize_docs.py:213:1
2026-01-26T14:33:47.5424266Z     |
2026-01-26T14:33:47.5424349Z 211 |                     if not self.dry_run:
2026-01-26T14:33:47.5424433Z 212 |                         md_file.unlink()
2026-01-26T14:33:47.5424497Z 213 |                     
2026-01-26T14:33:47.5424562Z     | ^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5424807Z 214 |                     self.changes.append(f"- Deleted empty file `{md_file.relative_to(self.root_dir)}`")
2026-01-26T14:33:47.5424910Z 215 |                     self.stats["deleted"] += 1
2026-01-26T14:33:47.5424968Z     |
2026-01-26T14:33:47.5425053Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5425057Z 
2026-01-26T14:33:47.5425143Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5425227Z    --> scripts/organize_docs.py:218:1
2026-01-26T14:33:47.5425285Z     |
2026-01-26T14:33:47.5425373Z 216 |             except Exception as e:
2026-01-26T14:33:47.5425505Z 217 |                 self.log(f"Error reading {md_file}: {e}", "ERROR")
2026-01-26T14:33:47.5425567Z 218 |     
2026-01-26T14:33:47.5425625Z     | ^^^^
2026-01-26T14:33:47.5425709Z 219 |     def generate_report(self):
2026-01-26T14:33:47.5425806Z 220 |         """Generate organization report"""
2026-01-26T14:33:47.5425865Z     |
2026-01-26T14:33:47.5425954Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5425959Z 
2026-01-26T14:33:47.5426041Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5426124Z    --> scripts/organize_docs.py:224:1
2026-01-26T14:33:47.5426186Z     |
2026-01-26T14:33:47.5426372Z 222 |         print("📊 DOCUMENTATION ORGANIZATION REPORT")
2026-01-26T14:33:47.5426446Z 223 |         print("=" * 60)
2026-01-26T14:33:47.5426506Z 224 |         
2026-01-26T14:33:47.5426574Z     | ^^^^^^^^
2026-01-26T14:33:47.5426737Z 225 |         if self.dry_run:
2026-01-26T14:33:47.5426914Z 226 |             print("🔍 DRY RUN MODE - No changes made\n")
2026-01-26T14:33:47.5426978Z     |
2026-01-26T14:33:47.5427062Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5427191Z 
2026-01-26T14:33:47.5427275Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5427361Z    --> scripts/organize_docs.py:227:1
2026-01-26T14:33:47.5427420Z     |
2026-01-26T14:33:47.5427491Z 225 |         if self.dry_run:
2026-01-26T14:33:47.5427656Z 226 |             print("🔍 DRY RUN MODE - No changes made\n")
2026-01-26T14:33:47.5427722Z 227 |         
2026-01-26T14:33:47.5427781Z     | ^^^^^^^^
2026-01-26T14:33:47.5427949Z 228 |         print(f"📁 Root Directory: {self.root_dir}\n")
2026-01-26T14:33:47.5428013Z     |
2026-01-26T14:33:47.5428098Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5428103Z 
2026-01-26T14:33:47.5428183Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5428273Z    --> scripts/organize_docs.py:229:1
2026-01-26T14:33:47.5428338Z     |
2026-01-26T14:33:47.5428497Z 228 |         print(f"📁 Root Directory: {self.root_dir}\n")
2026-01-26T14:33:47.5428558Z 229 |         
2026-01-26T14:33:47.5428623Z     | ^^^^^^^^
2026-01-26T14:33:47.5428743Z 230 |         print("📈 Statistics:")
2026-01-26T14:33:47.5428965Z 231 |         print(f"  - Files moved: {self.stats['moved']}")
2026-01-26T14:33:47.5429030Z     |
2026-01-26T14:33:47.5429116Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5429120Z 
2026-01-26T14:33:47.5429201Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5429280Z    --> scripts/organize_docs.py:235:1
2026-01-26T14:33:47.5429343Z     |
2026-01-26T14:33:47.5429505Z 233 |         print(f"  - Duplicates found: {self.stats['duplicates_found']}")
2026-01-26T14:33:47.5429650Z 234 |         print(f"  - Empty files deleted: {self.stats['deleted']}")
2026-01-26T14:33:47.5429715Z 235 |         
2026-01-26T14:33:47.5429777Z     | ^^^^^^^^
2026-01-26T14:33:47.5429857Z 236 |         if self.changes:
2026-01-26T14:33:47.5430239Z 237 |             print(f"\n📝 Changes ({len(self.changes)}):")
2026-01-26T14:33:47.5430305Z     |
2026-01-26T14:33:47.5430396Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5430401Z 
2026-01-26T14:33:47.5430492Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5430587Z    --> scripts/organize_docs.py:240:1
2026-01-26T14:33:47.5430646Z     |
2026-01-26T14:33:47.5430775Z 238 |             for change in self.changes[:20]:  # Limit to 20
2026-01-26T14:33:47.5430863Z 239 |                 print(f"  {change}")
2026-01-26T14:33:47.5430925Z 240 |             
2026-01-26T14:33:47.5430985Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5431074Z 241 |             if len(self.changes) > 20:
2026-01-26T14:33:47.5431211Z 242 |                 print(f"  ... and {len(self.changes) - 20} more")
2026-01-26T14:33:47.5431272Z     |
2026-01-26T14:33:47.5431359Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5431363Z 
2026-01-26T14:33:47.5431456Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5431540Z    --> scripts/organize_docs.py:243:1
2026-01-26T14:33:47.5431598Z     |
2026-01-26T14:33:47.5431692Z 241 |             if len(self.changes) > 20:
2026-01-26T14:33:47.5431820Z 242 |                 print(f"  ... and {len(self.changes) - 20} more")
2026-01-26T14:33:47.5431880Z 243 |         
2026-01-26T14:33:47.5431940Z     | ^^^^^^^^
2026-01-26T14:33:47.5432020Z 244 |         print("\n" + "=" * 60)
2026-01-26T14:33:47.5432078Z     |
2026-01-26T14:33:47.5432165Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5432169Z 
2026-01-26T14:33:47.5432253Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5432333Z    --> scripts/organize_docs.py:245:1
2026-01-26T14:33:47.5432391Z     |
2026-01-26T14:33:47.5432463Z 244 |         print("\n" + "=" * 60)
2026-01-26T14:33:47.5432528Z 245 |         
2026-01-26T14:33:47.5432586Z     | ^^^^^^^^
2026-01-26T14:33:47.5432658Z 246 |         if self.dry_run:
2026-01-26T14:33:47.5432991Z 247 |             print("💡 Run without --dry-run to apply changes")
2026-01-26T14:33:47.5433049Z     |
2026-01-26T14:33:47.5433133Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5433138Z 
2026-01-26T14:33:47.5433326Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5433412Z    --> scripts/organize_docs.py:250:1
2026-01-26T14:33:47.5433469Z     |
2026-01-26T14:33:47.5433536Z 248 |         else:
2026-01-26T14:33:47.5433691Z 249 |             print("✅ Organization complete!")
2026-01-26T14:33:47.5433752Z 250 |         
2026-01-26T14:33:47.5433811Z     | ^^^^^^^^
2026-01-26T14:33:47.5433886Z 251 |         print("=" * 60 + "\n")
2026-01-26T14:33:47.5433944Z     |
2026-01-26T14:33:47.5434027Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5434032Z 
2026-01-26T14:33:47.5434117Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5434198Z    --> scripts/organize_docs.py:252:1
2026-01-26T14:33:47.5434255Z     |
2026-01-26T14:33:47.5434324Z 251 |         print("=" * 60 + "\n")
2026-01-26T14:33:47.5434395Z 252 |     
2026-01-26T14:33:47.5434453Z     | ^^^^
2026-01-26T14:33:47.5434532Z 253 |     def create_docs_index(self):
2026-01-26T14:33:47.5434640Z 254 |         """Create/update docs/README.md index"""
2026-01-26T14:33:47.5434706Z     |
2026-01-26T14:33:47.5434792Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5434797Z 
2026-01-26T14:33:47.5434877Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5434964Z    --> scripts/organize_docs.py:258:1
2026-01-26T14:33:47.5435024Z     |
2026-01-26T14:33:47.5435160Z 256 |             self.log("Would create/update docs/README.md index")
2026-01-26T14:33:47.5435233Z 257 |             return
2026-01-26T14:33:47.5435292Z 258 |         
2026-01-26T14:33:47.5435350Z     | ^^^^^^^^
2026-01-26T14:33:47.5435512Z 259 |         # This is already created manually, so we skip auto-generation
2026-01-26T14:33:47.5435630Z 260 |         # In future, could parse and auto-generate
2026-01-26T14:33:47.5435692Z     |
2026-01-26T14:33:47.5435777Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5435782Z 
2026-01-26T14:33:47.5435866Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5435947Z    --> scripts/organize_docs.py:262:1
2026-01-26T14:33:47.5436004Z     |
2026-01-26T14:33:47.5436118Z 260 |         # In future, could parse and auto-generate
2026-01-26T14:33:47.5436239Z 261 |         self.log("Docs index exists at docs/README.md")
2026-01-26T14:33:47.5436298Z 262 |     
2026-01-26T14:33:47.5436357Z     | ^^^^
2026-01-26T14:33:47.5436430Z 263 |     def run(self):
2026-01-26T14:33:47.5436525Z 264 |         """Run the organization process"""
2026-01-26T14:33:47.5436583Z     |
2026-01-26T14:33:47.5436674Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5436679Z 
2026-01-26T14:33:47.5436760Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5436841Z    --> scripts/organize_docs.py:266:1
2026-01-26T14:33:47.5436904Z     |
2026-01-26T14:33:47.5436996Z 264 |         """Run the organization process"""
2026-01-26T14:33:47.5437151Z 265 |         self.log("Starting documentation organization...", "INFO")
2026-01-26T14:33:47.5437211Z 266 |         
2026-01-26T14:33:47.5437278Z     | ^^^^^^^^
2026-01-26T14:33:47.5437372Z 267 |         # Ensure docs structure exists
2026-01-26T14:33:47.5437449Z 268 |         if not self.dry_run:
2026-01-26T14:33:47.5437513Z     |
2026-01-26T14:33:47.5437598Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5437602Z 
2026-01-26T14:33:47.5437681Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5437766Z    --> scripts/organize_docs.py:273:1
2026-01-26T14:33:47.5437827Z     |
2026-01-26T14:33:47.5437971Z 271 |             (self.docs_dir / "api").mkdir(parents=True, exist_ok=True)
2026-01-26T14:33:47.5438105Z 272 |             self.archive_dir.mkdir(parents=True, exist_ok=True)
2026-01-26T14:33:47.5438170Z 273 |         
2026-01-26T14:33:47.5438229Z     | ^^^^^^^^
2026-01-26T14:33:47.5438307Z 274 |         # Find all markdown files
2026-01-26T14:33:47.5438501Z 275 |         md_files = self.find_markdown_files()
2026-01-26T14:33:47.5438559Z     |
2026-01-26T14:33:47.5438643Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5438648Z 
2026-01-26T14:33:47.5438928Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5439031Z    --> scripts/organize_docs.py:277:1
2026-01-26T14:33:47.5439091Z     |
2026-01-26T14:33:47.5439190Z 275 |         md_files = self.find_markdown_files()
2026-01-26T14:33:47.5439341Z 276 |         self.log(f"Found {len(md_files)} markdown files", "INFO")
2026-01-26T14:33:47.5439401Z 277 |         
2026-01-26T14:33:47.5439461Z     | ^^^^^^^^
2026-01-26T14:33:47.5439542Z 278 |         # Organize root files
2026-01-26T14:33:47.5439655Z 279 |         self.organize_root_files(md_files.copy())
2026-01-26T14:33:47.5439714Z     |
2026-01-26T14:33:47.5439798Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5439803Z 
2026-01-26T14:33:47.5439891Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5439975Z    --> scripts/organize_docs.py:280:1
2026-01-26T14:33:47.5440033Z     |
2026-01-26T14:33:47.5440113Z 278 |         # Organize root files
2026-01-26T14:33:47.5440219Z 279 |         self.organize_root_files(md_files.copy())
2026-01-26T14:33:47.5440278Z 280 |         
2026-01-26T14:33:47.5440341Z     | ^^^^^^^^
2026-01-26T14:33:47.5440425Z 281 |         # Archive versioned files
2026-01-26T14:33:47.5440579Z 282 |         md_files = self.find_markdown_files()  # Re-scan after moves
2026-01-26T14:33:47.5440638Z     |
2026-01-26T14:33:47.5440729Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5440734Z 
2026-01-26T14:33:47.5440814Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5440896Z    --> scripts/organize_docs.py:284:1
2026-01-26T14:33:47.5440959Z     |
2026-01-26T14:33:47.5441106Z 282 |         md_files = self.find_markdown_files()  # Re-scan after moves
2026-01-26T14:33:47.5441228Z 283 |         self.archive_versioned_files(md_files.copy())
2026-01-26T14:33:47.5441290Z 284 |         
2026-01-26T14:33:47.5441357Z     | ^^^^^^^^
2026-01-26T14:33:47.5441435Z 285 |         # Check for duplicates
2026-01-26T14:33:47.5441554Z 286 |         md_files = self.find_markdown_files()  # Re-scan
2026-01-26T14:33:47.5441617Z     |
2026-01-26T14:33:47.5441704Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5441709Z 
2026-01-26T14:33:47.5441791Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5441882Z    --> scripts/organize_docs.py:288:1
2026-01-26T14:33:47.5441940Z     |
2026-01-26T14:33:47.5442054Z 286 |         md_files = self.find_markdown_files()  # Re-scan
2026-01-26T14:33:47.5442148Z 287 |         self.check_duplicates(md_files)
2026-01-26T14:33:47.5442214Z 288 |         
2026-01-26T14:33:47.5442273Z     | ^^^^^^^^
2026-01-26T14:33:47.5442348Z 289 |         # Delete empty files
2026-01-26T14:33:47.5442467Z 290 |         md_files = self.find_markdown_files()  # Re-scan
2026-01-26T14:33:47.5442525Z     |
2026-01-26T14:33:47.5442609Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5442617Z 
2026-01-26T14:33:47.5442702Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5442784Z    --> scripts/organize_docs.py:292:1
2026-01-26T14:33:47.5442842Z     |
2026-01-26T14:33:47.5442955Z 290 |         md_files = self.find_markdown_files()  # Re-scan
2026-01-26T14:33:47.5443054Z 291 |         self.delete_empty_files(md_files)
2026-01-26T14:33:47.5443114Z 292 |         
2026-01-26T14:33:47.5443176Z     | ^^^^^^^^
2026-01-26T14:33:47.5443252Z 293 |         # Create index
2026-01-26T14:33:47.5443332Z 294 |         self.create_docs_index()
2026-01-26T14:33:47.5443390Z     |
2026-01-26T14:33:47.5443475Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5443479Z 
2026-01-26T14:33:47.5443566Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5443646Z    --> scripts/organize_docs.py:295:1
2026-01-26T14:33:47.5443703Z     |
2026-01-26T14:33:47.5443780Z 293 |         # Create index
2026-01-26T14:33:47.5443858Z 294 |         self.create_docs_index()
2026-01-26T14:33:47.5444036Z 295 |         
2026-01-26T14:33:47.5444096Z     | ^^^^^^^^
2026-01-26T14:33:47.5444177Z 296 |         # Generate report
2026-01-26T14:33:47.5444254Z 297 |         self.generate_report()
2026-01-26T14:33:47.5444312Z     |
2026-01-26T14:33:47.5444486Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5444493Z 
2026-01-26T14:33:47.5444576Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5444656Z    --> scripts/organize_docs.py:308:1
2026-01-26T14:33:47.5444718Z     |
2026-01-26T14:33:47.5444810Z 306 |   # Preview changes without applying
2026-01-26T14:33:47.5444916Z 307 |   python scripts/organize_docs.py --dry-run
2026-01-26T14:33:47.5444979Z 308 |   
2026-01-26T14:33:47.5445042Z     | ^^
2026-01-26T14:33:47.5445131Z 309 |   # Apply changes with verbose output
2026-01-26T14:33:47.5445231Z 310 |   python scripts/organize_docs.py --verbose
2026-01-26T14:33:47.5445294Z     |
2026-01-26T14:33:47.5445378Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5445388Z 
2026-01-26T14:33:47.5445467Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5445554Z    --> scripts/organize_docs.py:311:1
2026-01-26T14:33:47.5445612Z     |
2026-01-26T14:33:47.5445698Z 309 |   # Apply changes with verbose output
2026-01-26T14:33:47.5445812Z 310 |   python scripts/organize_docs.py --verbose
2026-01-26T14:33:47.5445876Z 311 |   
2026-01-26T14:33:47.5445933Z     | ^^
2026-01-26T14:33:47.5446013Z 312 |   # Apply changes silently
2026-01-26T14:33:47.5446102Z 313 |   python scripts/organize_docs.py
2026-01-26T14:33:47.5446161Z     |
2026-01-26T14:33:47.5446248Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5446254Z 
2026-01-26T14:33:47.5446335Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5446431Z    --> scripts/organize_docs.py:316:1
2026-01-26T14:33:47.5446490Z     |
2026-01-26T14:33:47.5446549Z 314 |         """
2026-01-26T14:33:47.5446613Z 315 |     )
2026-01-26T14:33:47.5446672Z 316 |     
2026-01-26T14:33:47.5446730Z     | ^^^^
2026-01-26T14:33:47.5446812Z 317 |     parser.add_argument(
2026-01-26T14:33:47.5446887Z 318 |         "--dry-run",
2026-01-26T14:33:47.5446945Z     |
2026-01-26T14:33:47.5447029Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5447034Z 
2026-01-26T14:33:47.5447123Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5447204Z    --> scripts/organize_docs.py:322:1
2026-01-26T14:33:47.5447262Z     |
2026-01-26T14:33:47.5447388Z 320 |         help="Preview changes without applying them"
2026-01-26T14:33:47.5447450Z 321 |     )
2026-01-26T14:33:47.5447508Z 322 |     
2026-01-26T14:33:47.5447566Z     | ^^^^
2026-01-26T14:33:47.5447647Z 323 |     parser.add_argument(
2026-01-26T14:33:47.5447716Z 324 |         "--verbose",
2026-01-26T14:33:47.5447773Z     |
2026-01-26T14:33:47.5447863Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5447867Z 
2026-01-26T14:33:47.5447947Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5448026Z    --> scripts/organize_docs.py:329:1
2026-01-26T14:33:47.5448088Z     |
2026-01-26T14:33:47.5448178Z 327 |         help="Show detailed output"
2026-01-26T14:33:47.5448237Z 328 |     )
2026-01-26T14:33:47.5448295Z 329 |     
2026-01-26T14:33:47.5448358Z     | ^^^^
2026-01-26T14:33:47.5448438Z 330 |     args = parser.parse_args()
2026-01-26T14:33:47.5448499Z     |
2026-01-26T14:33:47.5448582Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5448587Z 
2026-01-26T14:33:47.5448673Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5448753Z    --> scripts/organize_docs.py:331:1
2026-01-26T14:33:47.5448911Z     |
2026-01-26T14:33:47.5448998Z 330 |     args = parser.parse_args()
2026-01-26T14:33:47.5449057Z 331 |     
2026-01-26T14:33:47.5449114Z     | ^^^^
2026-01-26T14:33:47.5449234Z 332 |     # Determine project root (parent of scripts/)
2026-01-26T14:33:47.5449326Z 333 |     script_dir = Path(__file__).parent
2026-01-26T14:33:47.5449383Z     |
2026-01-26T14:33:47.5449467Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5449473Z 
2026-01-26T14:33:47.5449690Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5449774Z    --> scripts/organize_docs.py:335:1
2026-01-26T14:33:47.5449833Z     |
2026-01-26T14:33:47.5449925Z 333 |     script_dir = Path(__file__).parent
2026-01-26T14:33:47.5450105Z 334 |     root_dir = script_dir.parent
2026-01-26T14:33:47.5450167Z 335 |     
2026-01-26T14:33:47.5450225Z     | ^^^^
2026-01-26T14:33:47.5450454Z 336 |     organizer = DocsOrganizer(root_dir, dry_run=args.dry_run, verbose=args.verbose)
2026-01-26T14:33:47.5450529Z 337 |     organizer.run()
2026-01-26T14:33:47.5450587Z     |
2026-01-26T14:33:47.5450677Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5450683Z 
2026-01-26T14:33:47.5450788Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5450865Z  --> test_logging.py:2:1
2026-01-26T14:33:47.5450929Z   |
2026-01-26T14:33:47.5451007Z 1 |   """Tests for logging system"""
2026-01-26T14:33:47.5451072Z 2 | / import sys
2026-01-26T14:33:47.5451135Z 3 | | import os
2026-01-26T14:33:47.5451224Z 4 | | from pathlib import Path
2026-01-26T14:33:47.5451293Z   | |________________________^
2026-01-26T14:33:47.5451351Z 5 |
2026-01-26T14:33:47.5451439Z 6 |   sys.path.append(os.getcwd())
2026-01-26T14:33:47.5451496Z   |
2026-01-26T14:33:47.5451572Z help: Organize imports
2026-01-26T14:33:47.5451578Z 
2026-01-26T14:33:47.5451670Z F401 [*] `pathlib.Path` imported but unused
2026-01-26T14:33:47.5451754Z  --> test_logging.py:4:21
2026-01-26T14:33:47.5451811Z   |
2026-01-26T14:33:47.5451873Z 2 | import sys
2026-01-26T14:33:47.5451942Z 3 | import os
2026-01-26T14:33:47.5452019Z 4 | from pathlib import Path
2026-01-26T14:33:47.5452084Z   |                     ^^^^
2026-01-26T14:33:47.5452141Z 5 |
2026-01-26T14:33:47.5452226Z 6 | sys.path.append(os.getcwd())
2026-01-26T14:33:47.5452283Z   |
2026-01-26T14:33:47.5452379Z help: Remove unused import: `pathlib.Path`
2026-01-26T14:33:47.5452384Z 
2026-01-26T14:33:47.5452490Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5452563Z  --> test_logging.py:8:1
2026-01-26T14:33:47.5452627Z   |
2026-01-26T14:33:47.5452714Z 6 |   sys.path.append(os.getcwd())
2026-01-26T14:33:47.5452772Z 7 |
2026-01-26T14:33:47.5452874Z 8 | / from logger import setup_logger, get_logger
2026-01-26T14:33:47.5452961Z 9 | | from config import LOG_FILE, AI_DIR
2026-01-26T14:33:47.5453037Z   | |___________________________________^
2026-01-26T14:33:47.5453095Z   |
2026-01-26T14:33:47.5453168Z help: Organize imports
2026-01-26T14:33:47.5453173Z 
2026-01-26T14:33:47.5453268Z F401 [*] `config.AI_DIR` imported but unused
2026-01-26T14:33:47.5453342Z  --> test_logging.py:9:30
2026-01-26T14:33:47.5453400Z   |
2026-01-26T14:33:47.5453502Z 8 | from logger import setup_logger, get_logger
2026-01-26T14:33:47.5453590Z 9 | from config import LOG_FILE, AI_DIR
2026-01-26T14:33:47.5453657Z   |                              ^^^^^^
2026-01-26T14:33:47.5453715Z   |
2026-01-26T14:33:47.5453811Z help: Remove unused import: `config.AI_DIR`
2026-01-26T14:33:47.5453815Z 
2026-01-26T14:33:47.5453900Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5453978Z   --> test_logging.py:15:1
2026-01-26T14:33:47.5454041Z    |
2026-01-26T14:33:47.5454135Z 13 |     """Test logger can be initialized"""
2026-01-26T14:33:47.5454223Z 14 |     print("Testing logger setup...")
2026-01-26T14:33:47.5454283Z 15 |     
2026-01-26T14:33:47.5454346Z    | ^^^^
2026-01-26T14:33:47.5454434Z 16 |     logger = setup_logger("TestLogger")
2026-01-26T14:33:47.5454511Z 17 |     assert logger is not None
2026-01-26T14:33:47.5454574Z    |
2026-01-26T14:33:47.5454659Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5454663Z 
2026-01-26T14:33:47.5454744Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5454818Z   --> test_logging.py:20:1
2026-01-26T14:33:47.5454880Z    |
2026-01-26T14:33:47.5454964Z 18 |     assert logger.name == "TestLogger"
2026-01-26T14:33:47.5455047Z 19 |     print("  [OK] Logger initialized")
2026-01-26T14:33:47.5455110Z 20 |     
2026-01-26T14:33:47.5455167Z    | ^^^^
2026-01-26T14:33:47.5455318Z 21 |
2026-01-26T14:33:47.5455399Z 22 | def test_logger_singleton():
2026-01-26T14:33:47.5455462Z    |
2026-01-26T14:33:47.5455545Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5455549Z 
2026-01-26T14:33:47.5455702Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5455785Z   --> test_logging.py:25:1
2026-01-26T14:33:47.5455843Z    |
2026-01-26T14:33:47.5455922Z 23 |     """Test logger is singleton"""
2026-01-26T14:33:47.5456042Z 24 |     print("Testing logger singleton pattern...")
2026-01-26T14:33:47.5456100Z 25 |     
2026-01-26T14:33:47.5456157Z    | ^^^^
2026-01-26T14:33:47.5456233Z 26 |     logger1 = get_logger()
2026-01-26T14:33:47.5456310Z 27 |     logger2 = get_logger()
2026-01-26T14:33:47.5456370Z    |
2026-01-26T14:33:47.5456453Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5456458Z 
2026-01-26T14:33:47.5456542Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5456614Z   --> test_logging.py:35:1
2026-01-26T14:33:47.5456670Z    |
2026-01-26T14:33:47.5456760Z 33 |     """Test that log file is created"""
2026-01-26T14:33:47.5456858Z 34 |     print("Testing log file creation...")
2026-01-26T14:33:47.5456920Z 35 |     
2026-01-26T14:33:47.5456979Z    | ^^^^
2026-01-26T14:33:47.5457059Z 36 |     logger = get_logger()
2026-01-26T14:33:47.5457143Z 37 |     logger.info("Test log message")
2026-01-26T14:33:47.5457202Z    |
2026-01-26T14:33:47.5457287Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5457298Z 
2026-01-26T14:33:47.5457382Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5457455Z   --> test_logging.py:40:1
2026-01-26T14:33:47.5457513Z    |
2026-01-26T14:33:47.5457613Z 38 |     logger.warning("Test warning message")
2026-01-26T14:33:47.5457697Z 39 |     logger.error("Test error message")
2026-01-26T14:33:47.5457756Z 40 |     
2026-01-26T14:33:47.5457818Z    | ^^^^
2026-01-26T14:33:47.5457891Z 41 |     if LOG_FILE.exists():
2026-01-26T14:33:47.5458008Z 42 |         content = LOG_FILE.read_text(encoding='utf-8')
2026-01-26T14:33:47.5458069Z    |
2026-01-26T14:33:47.5458158Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5458164Z 
2026-01-26T14:33:47.5458244Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5458316Z   --> test_logging.py:54:1
2026-01-26T14:33:47.5458382Z    |
2026-01-26T14:33:47.5458464Z 52 |     """Test different log levels"""
2026-01-26T14:33:47.5458545Z 53 |     print("Testing log levels...")
2026-01-26T14:33:47.5458603Z 54 |     
2026-01-26T14:33:47.5458669Z    | ^^^^
2026-01-26T14:33:47.5458740Z 55 |     logger = get_logger()
2026-01-26T14:33:47.5458895Z    |
2026-01-26T14:33:47.5458992Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5458997Z 
2026-01-26T14:33:47.5459078Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5459157Z   --> test_logging.py:56:1
2026-01-26T14:33:47.5459221Z    |
2026-01-26T14:33:47.5459297Z 55 |     logger = get_logger()
2026-01-26T14:33:47.5459357Z 56 |     
2026-01-26T14:33:47.5459414Z    | ^^^^
2026-01-26T14:33:47.5459505Z 57 |     logger.debug("Debug message")
2026-01-26T14:33:47.5459581Z 58 |     logger.info("Info message")
2026-01-26T14:33:47.5459640Z    |
2026-01-26T14:33:47.5459728Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5459733Z 
2026-01-26T14:33:47.5459818Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5459892Z   --> test_logging.py:62:1
2026-01-26T14:33:47.5459948Z    |
2026-01-26T14:33:47.5460033Z 60 |     logger.error("Error message")
2026-01-26T14:33:47.5460125Z 61 |     logger.critical("Critical message")
2026-01-26T14:33:47.5460183Z 62 |     
2026-01-26T14:33:47.5460247Z    | ^^^^
2026-01-26T14:33:47.5460364Z 63 |     print("  [OK] All log levels work without errors")
2026-01-26T14:33:47.5460423Z    |
2026-01-26T14:33:47.5460509Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5460519Z 
2026-01-26T14:33:47.5460598Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5460672Z   --> test_logging.py:69:1
2026-01-26T14:33:47.5460729Z    |
2026-01-26T14:33:47.5460949Z 67 |     """Test log rotation configuration"""
2026-01-26T14:33:47.5461065Z 68 |     print("Testing log rotation configuration...")
2026-01-26T14:33:47.5461123Z 69 |     
2026-01-26T14:33:47.5461186Z    | ^^^^
2026-01-26T14:33:47.5461355Z 70 |     logger = get_logger()
2026-01-26T14:33:47.5461418Z    |
2026-01-26T14:33:47.5461505Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5461511Z 
2026-01-26T14:33:47.5461596Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5461668Z   --> test_logging.py:71:1
2026-01-26T14:33:47.5461726Z    |
2026-01-26T14:33:47.5461804Z 70 |     logger = get_logger()
2026-01-26T14:33:47.5461862Z 71 |     
2026-01-26T14:33:47.5461920Z    | ^^^^
2026-01-26T14:33:47.5462006Z 72 |     for handler in logger.handlers:
2026-01-26T14:33:47.5462101Z 73 |         if hasattr(handler, 'maxBytes'):
2026-01-26T14:33:47.5462159Z    |
2026-01-26T14:33:47.5462242Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5462247Z 
2026-01-26T14:33:47.5462332Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5462408Z   --> test_logging.py:78:1
2026-01-26T14:33:47.5462465Z    |
2026-01-26T14:33:47.5462748Z 76 |             print(f"  [OK] Log rotation configured: {handler.maxBytes} bytes, {handler.backupCount} backups")
2026-01-26T14:33:47.5462817Z 77 |             return
2026-01-26T14:33:47.5462876Z 78 |     
2026-01-26T14:33:47.5462933Z    | ^^^^
2026-01-26T14:33:47.5463061Z 79 |     print("  [WARNING] No rotating file handler found")
2026-01-26T14:33:47.5463119Z    |
2026-01-26T14:33:47.5463203Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5463208Z 
2026-01-26T14:33:47.5463293Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5463366Z   --> test_logging.py:87:1
2026-01-26T14:33:47.5463423Z    |
2026-01-26T14:33:47.5463496Z 85 |     print("=" * 50)
2026-01-26T14:33:47.5463559Z 86 |     print()
2026-01-26T14:33:47.5463617Z 87 |     
2026-01-26T14:33:47.5463675Z    | ^^^^
2026-01-26T14:33:47.5463742Z 88 |     try:
2026-01-26T14:33:47.5463820Z 89 |         test_logger_setup()
2026-01-26T14:33:47.5463879Z    |
2026-01-26T14:33:47.5463966Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5463977Z 
2026-01-26T14:33:47.5464058Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5464133Z   --> test_logging.py:94:1
2026-01-26T14:33:47.5464190Z    |
2026-01-26T14:33:47.5464267Z 92 |         test_log_levels()
2026-01-26T14:33:47.5464345Z 93 |         test_log_rotation_config()
2026-01-26T14:33:47.5464405Z 94 |         
2026-01-26T14:33:47.5464467Z    | ^^^^^^^^
2026-01-26T14:33:47.5464532Z 95 |         print()
2026-01-26T14:33:47.5464601Z 96 |         print("=" * 50)
2026-01-26T14:33:47.5464658Z    |
2026-01-26T14:33:47.5464748Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5464753Z 
2026-01-26T14:33:47.5464833Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5464908Z    --> test_logging.py:99:1
2026-01-26T14:33:47.5464972Z     |
2026-01-26T14:33:47.5465093Z  97 |         print("[SUCCESS] ALL LOGGING TESTS PASSED!")
2026-01-26T14:33:47.5465174Z  98 |         print("=" * 50)
2026-01-26T14:33:47.5465233Z  99 |         
2026-01-26T14:33:47.5465299Z     | ^^^^^^^^
2026-01-26T14:33:47.5465376Z 100 |         if LOG_FILE.exists():
2026-01-26T14:33:47.5465489Z 101 |             print(f"\nLog file location: {LOG_FILE}")
2026-01-26T14:33:47.5465555Z     |
2026-01-26T14:33:47.5465640Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5465646Z 
2026-01-26T14:33:47.5465737Z F401 [*] `pathlib.Path` imported but unused
2026-01-26T14:33:47.5465819Z  --> test_mcp_tools.py:3:21
2026-01-26T14:33:47.5465877Z   |
2026-01-26T14:33:47.5465946Z 1 | import os
2026-01-26T14:33:47.5466011Z 2 | import sys
2026-01-26T14:33:47.5466095Z 3 | from pathlib import Path
2026-01-26T14:33:47.5466161Z   |                     ^^^^
2026-01-26T14:33:47.5466219Z 4 |
2026-01-26T14:33:47.5466307Z 5 | sys.path.append(os.getcwd())
2026-01-26T14:33:47.5466365Z   |
2026-01-26T14:33:47.5471574Z help: Remove unused import: `pathlib.Path`
2026-01-26T14:33:47.5471757Z 
2026-01-26T14:33:47.5471908Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5472004Z   --> test_mcp_tools.py:8:5
2026-01-26T14:33:47.5472066Z    |
2026-01-26T14:33:47.5472129Z  7 |   try:
2026-01-26T14:33:47.5472315Z  8 | /     from mcp_server import (
2026-01-26T14:33:47.5472398Z  9 | |         read_memory,
2026-01-26T14:33:47.5472474Z 10 | |         update_memory,
2026-01-26T14:33:47.5472545Z 11 | |         clear_memory,
2026-01-26T14:33:47.5472633Z 12 | |         delete_memory_section,
2026-01-26T14:33:47.5472708Z 13 | |         index_codebase,
2026-01-26T14:33:47.5472787Z 14 | |         index_changed_files,
2026-01-26T14:33:47.5472863Z 15 | |         search_codebase,
2026-01-26T14:33:47.5472959Z 16 | |         search_codebase_advanced,
2026-01-26T14:33:47.5473034Z 17 | |         get_index_stats,
2026-01-26T14:33:47.5473110Z 18 | |         ingest_git_history,
2026-01-26T14:33:47.5473201Z 19 | |         generate_project_summary,
2026-01-26T14:33:47.5473275Z 20 | |         extract_tech_stack,
2026-01-26T14:33:47.5473363Z 21 | |         analyze_project_structure,
2026-01-26T14:33:47.5473452Z 22 | |         get_recent_changes_summary,
2026-01-26T14:33:47.5473549Z 23 | |         auto_update_memory_from_commits,
2026-01-26T14:33:47.5473636Z 24 | |         analyze_code_complexity,
2026-01-26T14:33:47.5473713Z 25 | |         analyze_code_quality,
2026-01-26T14:33:47.5473800Z 26 | |         get_test_coverage_info,
2026-01-26T14:33:47.5473875Z 27 | |         save_memory_version,
2026-01-26T14:33:47.5473949Z 28 | |         list_memory_versions,
2026-01-26T14:33:47.5474031Z 29 | |         restore_memory_version,
2026-01-26T14:33:47.5474093Z 30 | |     )
2026-01-26T14:33:47.5474153Z    | |_____^
2026-01-26T14:33:47.5474211Z 31 |
2026-01-26T14:33:47.5474319Z 32 |       print("Successfully imported tools.")
2026-01-26T14:33:47.5474377Z    |
2026-01-26T14:33:47.5474454Z help: Organize imports
2026-01-26T14:33:47.5474460Z 
2026-01-26T14:33:47.5474801Z F401 `mcp_server.clear_memory` imported but unused; consider using `importlib.util.find_spec` to test for availability
2026-01-26T14:33:47.5474891Z   --> test_mcp_tools.py:11:9
2026-01-26T14:33:47.5474952Z    |
2026-01-26T14:33:47.5475028Z  9 |         read_memory,
2026-01-26T14:33:47.5475103Z 10 |         update_memory,
2026-01-26T14:33:47.5475173Z 11 |         clear_memory,
2026-01-26T14:33:47.5475239Z    |         ^^^^^^^^^^^^
2026-01-26T14:33:47.5475320Z 12 |         delete_memory_section,
2026-01-26T14:33:47.5475390Z 13 |         index_codebase,
2026-01-26T14:33:47.5475449Z    |
2026-01-26T14:33:47.5475531Z help: Remove unused import
2026-01-26T14:33:47.5475536Z 
2026-01-26T14:33:47.5475887Z F401 `mcp_server.analyze_code_quality` imported but unused; consider using `importlib.util.find_spec` to test for availability
2026-01-26T14:33:47.5475964Z   --> test_mcp_tools.py:25:9
2026-01-26T14:33:47.5476023Z    |
2026-01-26T14:33:47.5476122Z 23 |         auto_update_memory_from_commits,
2026-01-26T14:33:47.5476204Z 24 |         analyze_code_complexity,
2026-01-26T14:33:47.5476283Z 25 |         analyze_code_quality,
2026-01-26T14:33:47.5476358Z    |         ^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5476437Z 26 |         get_test_coverage_info,
2026-01-26T14:33:47.5476511Z 27 |         save_memory_version,
2026-01-26T14:33:47.5476577Z    |
2026-01-26T14:33:47.5476654Z help: Remove unused import
2026-01-26T14:33:47.5476659Z 
2026-01-26T14:33:47.5477009Z F401 `mcp_server.restore_memory_version` imported but unused; consider using `importlib.util.find_spec` to test for availability
2026-01-26T14:33:47.5477086Z   --> test_mcp_tools.py:29:9
2026-01-26T14:33:47.5477152Z    |
2026-01-26T14:33:47.5477227Z 27 |         save_memory_version,
2026-01-26T14:33:47.5477302Z 28 |         list_memory_versions,
2026-01-26T14:33:47.5477384Z 29 |         restore_memory_version,
2026-01-26T14:33:47.5477452Z    |         ^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5477513Z 30 |     )
2026-01-26T14:33:47.5477572Z    |
2026-01-26T14:33:47.5477653Z help: Remove unused import
2026-01-26T14:33:47.5477792Z 
2026-01-26T14:33:47.5477903Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5477987Z  --> test_memory_limits.py:1:1
2026-01-26T14:33:47.5478052Z   |
2026-01-26T14:33:47.5478117Z 1 | / import sys
2026-01-26T14:33:47.5478253Z 2 | | import os
2026-01-26T14:33:47.5478321Z   | |_________^
2026-01-26T14:33:47.5478379Z 3 |
2026-01-26T14:33:47.5478461Z 4 |   sys.path.append(os.getcwd())
2026-01-26T14:33:47.5478519Z   |
2026-01-26T14:33:47.5478599Z help: Organize imports
2026-01-26T14:33:47.5478605Z 
2026-01-26T14:33:47.5478693Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5478904Z   --> test_memory_limits.py:12:1
2026-01-26T14:33:47.5478971Z    |
2026-01-26T14:33:47.5479087Z 10 |     """Test basic chunk addition and retrieval"""
2026-01-26T14:33:47.5479181Z 11 |     print("Testing basic indexing...")
2026-01-26T14:33:47.5479242Z 12 |     
2026-01-26T14:33:47.5479307Z    | ^^^^
2026-01-26T14:33:47.5479375Z 13 |     batches = []
2026-01-26T14:33:47.5479439Z    |
2026-01-26T14:33:47.5479530Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5479535Z 
2026-01-26T14:33:47.5479615Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5479693Z   --> test_memory_limits.py:14:1
2026-01-26T14:33:47.5479759Z    |
2026-01-26T14:33:47.5479828Z 13 |     batches = []
2026-01-26T14:33:47.5479890Z 14 |     
2026-01-26T14:33:47.5479950Z    | ^^^^
2026-01-26T14:33:47.5480071Z 15 |     def collect_batch(documents, metadatas, ids):
2026-01-26T14:33:47.5480250Z 16 |         batches.append((documents.copy(), metadatas.copy(), ids.copy()))
2026-01-26T14:33:47.5480310Z    |
2026-01-26T14:33:47.5480402Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5480408Z 
2026-01-26T14:33:47.5480489Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5480570Z   --> test_memory_limits.py:17:1
2026-01-26T14:33:47.5480628Z    |
2026-01-26T14:33:47.5480740Z 15 |     def collect_batch(documents, metadatas, ids):
2026-01-26T14:33:47.5480901Z 16 |         batches.append((documents.copy(), metadatas.copy(), ids.copy()))
2026-01-26T14:33:47.5480966Z 17 |     
2026-01-26T14:33:47.5481031Z    | ^^^^
2026-01-26T14:33:47.5481175Z 18 |     indexer = MemoryLimitedIndexer(1024 * 1024, collect_batch)
2026-01-26T14:33:47.5481234Z    |
2026-01-26T14:33:47.5481328Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5481334Z 
2026-01-26T14:33:47.5481415Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5481495Z   --> test_memory_limits.py:19:1
2026-01-26T14:33:47.5481555Z    |
2026-01-26T14:33:47.5481696Z 18 |     indexer = MemoryLimitedIndexer(1024 * 1024, collect_batch)
2026-01-26T14:33:47.5481755Z 19 |     
2026-01-26T14:33:47.5481815Z    | ^^^^
2026-01-26T14:33:47.5482000Z 20 |     indexer.add_chunk("test document 1", {"source": "file1.py"}, "file1_0")
2026-01-26T14:33:47.5482167Z 21 |     indexer.add_chunk("test document 2", {"source": "file2.py"}, "file2_0")
2026-01-26T14:33:47.5482226Z    |
2026-01-26T14:33:47.5482316Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5482330Z 
2026-01-26T14:33:47.5482413Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5482493Z   --> test_memory_limits.py:22:1
2026-01-26T14:33:47.5482553Z    |
2026-01-26T14:33:47.5482735Z 20 |     indexer.add_chunk("test document 1", {"source": "file1.py"}, "file1_0")
2026-01-26T14:33:47.5482902Z 21 |     indexer.add_chunk("test document 2", {"source": "file2.py"}, "file2_0")
2026-01-26T14:33:47.5482961Z 22 |     
2026-01-26T14:33:47.5483024Z    | ^^^^
2026-01-26T14:33:47.5483103Z 23 |     stats = indexer.get_stats()
2026-01-26T14:33:47.5483191Z 24 |     assert stats["total_chunks"] == 2
2026-01-26T14:33:47.5483250Z    |
2026-01-26T14:33:47.5483343Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5483347Z 
2026-01-26T14:33:47.5483427Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5483506Z   --> test_memory_limits.py:27:1
2026-01-26T14:33:47.5483570Z    |
2026-01-26T14:33:47.5483671Z 25 |     assert stats["current_buffer_chunks"] == 2
2026-01-26T14:33:47.5483881Z 26 |     assert len(batches) == 0
2026-01-26T14:33:47.5483947Z 27 |     
2026-01-26T14:33:47.5484006Z    | ^^^^
2026-01-26T14:33:47.5484095Z 28 |     print("  [OK] Basic indexing works")
2026-01-26T14:33:47.5484154Z    |
2026-01-26T14:33:47.5484345Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5484351Z 
2026-01-26T14:33:47.5484433Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5484514Z   --> test_memory_limits.py:34:1
2026-01-26T14:33:47.5484578Z    |
2026-01-26T14:33:47.5484719Z 32 |     """Test that indexer flushes when memory limit reached"""
2026-01-26T14:33:47.5484830Z 33 |     print("Testing memory limit auto-flush...")
2026-01-26T14:33:47.5484890Z 34 |     
2026-01-26T14:33:47.5484954Z    | ^^^^
2026-01-26T14:33:47.5485021Z 35 |     batches = []
2026-01-26T14:33:47.5485079Z    |
2026-01-26T14:33:47.5485170Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5485175Z 
2026-01-26T14:33:47.5485255Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5485337Z   --> test_memory_limits.py:36:1
2026-01-26T14:33:47.5485399Z    |
2026-01-26T14:33:47.5485464Z 35 |     batches = []
2026-01-26T14:33:47.5485523Z 36 |     
2026-01-26T14:33:47.5485581Z    | ^^^^
2026-01-26T14:33:47.5485704Z 37 |     def collect_batch(documents, metadatas, ids):
2026-01-26T14:33:47.5485874Z 38 |         batches.append((documents.copy(), metadatas.copy(), ids.copy()))
2026-01-26T14:33:47.5485933Z    |
2026-01-26T14:33:47.5486022Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5486026Z 
2026-01-26T14:33:47.5486107Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5486187Z   --> test_memory_limits.py:39:1
2026-01-26T14:33:47.5486246Z    |
2026-01-26T14:33:47.5486355Z 37 |     def collect_batch(documents, metadatas, ids):
2026-01-26T14:33:47.5486515Z 38 |         batches.append((documents.copy(), metadatas.copy(), ids.copy()))
2026-01-26T14:33:47.5486573Z 39 |     
2026-01-26T14:33:47.5486640Z    | ^^^^
2026-01-26T14:33:47.5486713Z 40 |     small_limit = 500
2026-01-26T14:33:47.5486864Z 41 |     indexer = MemoryLimitedIndexer(small_limit, collect_batch)
2026-01-26T14:33:47.5486927Z    |
2026-01-26T14:33:47.5487011Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5487015Z 
2026-01-26T14:33:47.5487098Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5487176Z   --> test_memory_limits.py:42:1
2026-01-26T14:33:47.5487240Z    |
2026-01-26T14:33:47.5487311Z 40 |     small_limit = 500
2026-01-26T14:33:47.5487453Z 41 |     indexer = MemoryLimitedIndexer(small_limit, collect_batch)
2026-01-26T14:33:47.5487518Z 42 |     
2026-01-26T14:33:47.5487579Z    | ^^^^
2026-01-26T14:33:47.5487655Z 43 |     large_doc = "x" * 200
2026-01-26T14:33:47.5487713Z    |
2026-01-26T14:33:47.5487801Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5487805Z 
2026-01-26T14:33:47.5487884Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5487961Z   --> test_memory_limits.py:44:1
2026-01-26T14:33:47.5488025Z    |
2026-01-26T14:33:47.5488096Z 43 |     large_doc = "x" * 200
2026-01-26T14:33:47.5488160Z 44 |     
2026-01-26T14:33:47.5488224Z    | ^^^^
2026-01-26T14:33:47.5488378Z 45 |     indexer.add_chunk(large_doc, {"source": "file1.py"}, "file1_0")
2026-01-26T14:33:47.5488459Z 46 |     initial_batches = len(batches)
2026-01-26T14:33:47.5488522Z    |
2026-01-26T14:33:47.5488612Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5488617Z 
2026-01-26T14:33:47.5488699Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5488886Z   --> test_memory_limits.py:47:1
2026-01-26T14:33:47.5488952Z    |
2026-01-26T14:33:47.5489099Z 45 |     indexer.add_chunk(large_doc, {"source": "file1.py"}, "file1_0")
2026-01-26T14:33:47.5489183Z 46 |     initial_batches = len(batches)
2026-01-26T14:33:47.5489243Z 47 |     
2026-01-26T14:33:47.5489308Z    | ^^^^
2026-01-26T14:33:47.5489457Z 48 |     indexer.add_chunk(large_doc, {"source": "file2.py"}, "file2_0")
2026-01-26T14:33:47.5489517Z    |
2026-01-26T14:33:47.5489612Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5489736Z 
2026-01-26T14:33:47.5489822Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5489904Z   --> test_memory_limits.py:49:1
2026-01-26T14:33:47.5489968Z    |
2026-01-26T14:33:47.5490217Z 48 |     indexer.add_chunk(large_doc, {"source": "file2.py"}, "file2_0")
2026-01-26T14:33:47.5490280Z 49 |     
2026-01-26T14:33:47.5490338Z    | ^^^^
2026-01-26T14:33:47.5490431Z 50 |     if len(batches) > initial_batches:
2026-01-26T14:33:47.5490512Z 51 |         assert len(batches[0][0]) >= 1
2026-01-26T14:33:47.5490572Z    |
2026-01-26T14:33:47.5490662Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5490667Z 
2026-01-26T14:33:47.5490748Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5490826Z   --> test_memory_limits.py:53:1
2026-01-26T14:33:47.5490884Z    |
2026-01-26T14:33:47.5490966Z 51 |         assert len(batches[0][0]) >= 1
2026-01-26T14:33:47.5491257Z 52 |         print(f"  [DEBUG] Auto-flush triggered: {len(batches)} batches, first batch has {len(batches[0][0])} docs")
2026-01-26T14:33:47.5491321Z 53 |     
2026-01-26T14:33:47.5491386Z    | ^^^^
2026-01-26T14:33:47.5491534Z 54 |     indexer.add_chunk(large_doc, {"source": "file3.py"}, "file3_0")
2026-01-26T14:33:47.5491610Z 55 |     indexer.flush()
2026-01-26T14:33:47.5491678Z    |
2026-01-26T14:33:47.5491763Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5491769Z 
2026-01-26T14:33:47.5491852Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5491931Z   --> test_memory_limits.py:56:1
2026-01-26T14:33:47.5491995Z    |
2026-01-26T14:33:47.5492137Z 54 |     indexer.add_chunk(large_doc, {"source": "file3.py"}, "file3_0")
2026-01-26T14:33:47.5492208Z 55 |     indexer.flush()
2026-01-26T14:33:47.5492273Z 56 |     
2026-01-26T14:33:47.5492332Z    | ^^^^
2026-01-26T14:33:47.5492481Z 57 |     assert len(batches) > 0, "At least one batch should be flushed"
2026-01-26T14:33:47.5492544Z    |
2026-01-26T14:33:47.5492632Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5492636Z 
2026-01-26T14:33:47.5492722Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5492804Z   --> test_memory_limits.py:58:1
2026-01-26T14:33:47.5492868Z    |
2026-01-26T14:33:47.5493007Z 57 |     assert len(batches) > 0, "At least one batch should be flushed"
2026-01-26T14:33:47.5493069Z 58 |     
2026-01-26T14:33:47.5493131Z    | ^^^^
2026-01-26T14:33:47.5493209Z 59 |     stats = indexer.get_stats()
2026-01-26T14:33:47.5493294Z 60 |     assert stats["total_chunks"] == 3
2026-01-26T14:33:47.5493352Z    |
2026-01-26T14:33:47.5493439Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5493444Z 
2026-01-26T14:33:47.5493525Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5493605Z   --> test_memory_limits.py:62:1
2026-01-26T14:33:47.5493670Z    |
2026-01-26T14:33:47.5493755Z 60 |     assert stats["total_chunks"] == 3
2026-01-26T14:33:47.5493860Z 61 |     assert stats["current_buffer_chunks"] == 0
2026-01-26T14:33:47.5493926Z 62 |     
2026-01-26T14:33:47.5493985Z    | ^^^^
2026-01-26T14:33:47.5494209Z 63 |     print(f"  [OK] Memory limit triggers flush (total batches: {stats['total_batches']})")
2026-01-26T14:33:47.5494268Z    |
2026-01-26T14:33:47.5494361Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5494365Z 
2026-01-26T14:33:47.5494451Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5494529Z   --> test_memory_limits.py:69:1
2026-01-26T14:33:47.5494594Z    |
2026-01-26T14:33:47.5494679Z 67 |     """Test manual flush operation"""
2026-01-26T14:33:47.5494765Z 68 |     print("Testing manual flush...")
2026-01-26T14:33:47.5494828Z 69 |     
2026-01-26T14:33:47.5494894Z    | ^^^^
2026-01-26T14:33:47.5494962Z 70 |     batches = []
2026-01-26T14:33:47.5495020Z    |
2026-01-26T14:33:47.5495114Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5495118Z 
2026-01-26T14:33:47.5495205Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5495282Z   --> test_memory_limits.py:71:1
2026-01-26T14:33:47.5495348Z    |
2026-01-26T14:33:47.5495415Z 70 |     batches = []
2026-01-26T14:33:47.5495566Z 71 |     
2026-01-26T14:33:47.5495625Z    | ^^^^
2026-01-26T14:33:47.5495745Z 72 |     def collect_batch(documents, metadatas, ids):
2026-01-26T14:33:47.5495833Z 73 |         batches.append(len(documents))
2026-01-26T14:33:47.5495892Z    |
2026-01-26T14:33:47.5496053Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5496059Z 
2026-01-26T14:33:47.5496140Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5496218Z   --> test_memory_limits.py:74:1
2026-01-26T14:33:47.5496277Z    |
2026-01-26T14:33:47.5496389Z 72 |     def collect_batch(documents, metadatas, ids):
2026-01-26T14:33:47.5496474Z 73 |         batches.append(len(documents))
2026-01-26T14:33:47.5496535Z 74 |     
2026-01-26T14:33:47.5496600Z    | ^^^^
2026-01-26T14:33:47.5496750Z 75 |     indexer = MemoryLimitedIndexer(10 * 1024 * 1024, collect_batch)
2026-01-26T14:33:47.5496809Z    |
2026-01-26T14:33:47.5496898Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5496903Z 
2026-01-26T14:33:47.5496987Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5497066Z   --> test_memory_limits.py:76:1
2026-01-26T14:33:47.5497125Z    |
2026-01-26T14:33:47.5497275Z 75 |     indexer = MemoryLimitedIndexer(10 * 1024 * 1024, collect_batch)
2026-01-26T14:33:47.5497338Z 76 |     
2026-01-26T14:33:47.5497398Z    | ^^^^
2026-01-26T14:33:47.5497477Z 77 |     for i in range(5):
2026-01-26T14:33:47.5497651Z 78 |         indexer.add_chunk(f"doc {i}", {"source": f"file{i}.py"}, f"file{i}_0")
2026-01-26T14:33:47.5497711Z    |
2026-01-26T14:33:47.5497797Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5497806Z 
2026-01-26T14:33:47.5497890Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5497969Z   --> test_memory_limits.py:79:1
2026-01-26T14:33:47.5498028Z    |
2026-01-26T14:33:47.5498108Z 77 |     for i in range(5):
2026-01-26T14:33:47.5498271Z 78 |         indexer.add_chunk(f"doc {i}", {"source": f"file{i}.py"}, f"file{i}_0")
2026-01-26T14:33:47.5498332Z 79 |     
2026-01-26T14:33:47.5498399Z    | ^^^^
2026-01-26T14:33:47.5498477Z 80 |     assert len(batches) == 0
2026-01-26T14:33:47.5498536Z    |
2026-01-26T14:33:47.5498620Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5498625Z 
2026-01-26T14:33:47.5498714Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5498892Z   --> test_memory_limits.py:81:1
2026-01-26T14:33:47.5498952Z    |
2026-01-26T14:33:47.5499033Z 80 |     assert len(batches) == 0
2026-01-26T14:33:47.5499093Z 81 |     
2026-01-26T14:33:47.5499153Z    | ^^^^
2026-01-26T14:33:47.5499226Z 82 |     indexer.flush()
2026-01-26T14:33:47.5499306Z 83 |     assert len(batches) == 1
2026-01-26T14:33:47.5499365Z    |
2026-01-26T14:33:47.5499449Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5499454Z 
2026-01-26T14:33:47.5499539Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5499617Z   --> test_memory_limits.py:85:1
2026-01-26T14:33:47.5499676Z    |
2026-01-26T14:33:47.5499758Z 83 |     assert len(batches) == 1
2026-01-26T14:33:47.5499837Z 84 |     assert batches[0] == 5
2026-01-26T14:33:47.5499895Z 85 |     
2026-01-26T14:33:47.5499953Z    | ^^^^
2026-01-26T14:33:47.5500028Z 86 |     indexer.flush()
2026-01-26T14:33:47.5500103Z 87 |     assert len(batches) == 1
2026-01-26T14:33:47.5500163Z    |
2026-01-26T14:33:47.5500256Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5500261Z 
2026-01-26T14:33:47.5500342Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5500420Z   --> test_memory_limits.py:88:1
2026-01-26T14:33:47.5500478Z    |
2026-01-26T14:33:47.5500554Z 86 |     indexer.flush()
2026-01-26T14:33:47.5500629Z 87 |     assert len(batches) == 1
2026-01-26T14:33:47.5500688Z 88 |     
2026-01-26T14:33:47.5500751Z    | ^^^^
2026-01-26T14:33:47.5500860Z 89 |     print("  [OK] Manual flush works correctly")
2026-01-26T14:33:47.5500920Z    |
2026-01-26T14:33:47.5501003Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5501008Z 
2026-01-26T14:33:47.5501099Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5501294Z   --> test_memory_limits.py:95:1
2026-01-26T14:33:47.5501354Z    |
2026-01-26T14:33:47.5501443Z 93 |     """Test memory size estimation"""
2026-01-26T14:33:47.5501540Z 94 |     print("Testing memory estimation...")
2026-01-26T14:33:47.5501599Z 95 |     
2026-01-26T14:33:47.5501761Z    | ^^^^
2026-01-26T14:33:47.5501831Z 96 |     batches = []
2026-01-26T14:33:47.5501903Z 97 |     flush_count = [0]
2026-01-26T14:33:47.5501962Z    |
2026-01-26T14:33:47.5502052Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5502057Z 
2026-01-26T14:33:47.5502137Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5502216Z    --> test_memory_limits.py:98:1
2026-01-26T14:33:47.5502281Z     |
2026-01-26T14:33:47.5502349Z  96 |     batches = []
2026-01-26T14:33:47.5502420Z  97 |     flush_count = [0]
2026-01-26T14:33:47.5502482Z  98 |     
2026-01-26T14:33:47.5502546Z     | ^^^^
2026-01-26T14:33:47.5502656Z  99 |     def count_flush(documents, metadatas, ids):
2026-01-26T14:33:47.5502729Z 100 |         flush_count[0] += 1
2026-01-26T14:33:47.5502798Z     |
2026-01-26T14:33:47.5502883Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5502888Z 
2026-01-26T14:33:47.5502969Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5503059Z    --> test_memory_limits.py:102:1
2026-01-26T14:33:47.5503119Z     |
2026-01-26T14:33:47.5503190Z 100 |         flush_count[0] += 1
2026-01-26T14:33:47.5503285Z 101 |         batches.append(len(documents))
2026-01-26T14:33:47.5503350Z 102 |     
2026-01-26T14:33:47.5503409Z     | ^^^^
2026-01-26T14:33:47.5503475Z 103 |     limit = 5000
2026-01-26T14:33:47.5503611Z 104 |     indexer = MemoryLimitedIndexer(limit, count_flush)
2026-01-26T14:33:47.5503675Z     |
2026-01-26T14:33:47.5503763Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5503768Z 
2026-01-26T14:33:47.5503848Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5503933Z    --> test_memory_limits.py:105:1
2026-01-26T14:33:47.5503993Z     |
2026-01-26T14:33:47.5504060Z 103 |     limit = 5000
2026-01-26T14:33:47.5504191Z 104 |     indexer = MemoryLimitedIndexer(limit, count_flush)
2026-01-26T14:33:47.5504251Z 105 |     
2026-01-26T14:33:47.5504313Z     | ^^^^
2026-01-26T14:33:47.5504387Z 106 |     for i in range(20):
2026-01-26T14:33:47.5504508Z 107 |         doc = f"This is document number {i} " * 10
2026-01-26T14:33:47.5504568Z     |
2026-01-26T14:33:47.5504654Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5504659Z 
2026-01-26T14:33:47.5504745Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5504824Z    --> test_memory_limits.py:109:1
2026-01-26T14:33:47.5504883Z     |
2026-01-26T14:33:47.5504994Z 107 |         doc = f"This is document number {i} " * 10
2026-01-26T14:33:47.5505180Z 108 |         indexer.add_chunk(doc, {"source": f"file{i}.py", "index": i}, f"id_{i}")
2026-01-26T14:33:47.5505240Z 109 |     
2026-01-26T14:33:47.5505302Z     | ^^^^
2026-01-26T14:33:47.5505378Z 110 |     indexer.flush()
2026-01-26T14:33:47.5505443Z     |
2026-01-26T14:33:47.5505531Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5505541Z 
2026-01-26T14:33:47.5505624Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5505703Z    --> test_memory_limits.py:111:1
2026-01-26T14:33:47.5505763Z     |
2026-01-26T14:33:47.5505845Z 110 |     indexer.flush()
2026-01-26T14:33:47.5505905Z 111 |     
2026-01-26T14:33:47.5505963Z     | ^^^^
2026-01-26T14:33:47.5506045Z 112 |     assert flush_count[0] > 0
2026-01-26T14:33:47.5506105Z     |
2026-01-26T14:33:47.5506189Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5506194Z 
2026-01-26T14:33:47.5506273Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5506357Z    --> test_memory_limits.py:113:1
2026-01-26T14:33:47.5506418Z     |
2026-01-26T14:33:47.5506495Z 112 |     assert flush_count[0] > 0
2026-01-26T14:33:47.5506561Z 113 |     
2026-01-26T14:33:47.5506621Z     | ^^^^
2026-01-26T14:33:47.5506699Z 114 |     stats = indexer.get_stats()
2026-01-26T14:33:47.5506791Z 115 |     assert stats["total_chunks"] == 20
2026-01-26T14:33:47.5506943Z     |
2026-01-26T14:33:47.5507028Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5507033Z 
2026-01-26T14:33:47.5507112Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5507270Z    --> test_memory_limits.py:117:1
2026-01-26T14:33:47.5507330Z     |
2026-01-26T14:33:47.5507419Z 115 |     assert stats["total_chunks"] == 20
2026-01-26T14:33:47.5507529Z 116 |     assert stats["current_buffer_chunks"] == 0
2026-01-26T14:33:47.5507588Z 117 |     
2026-01-26T14:33:47.5507647Z     | ^^^^
2026-01-26T14:33:47.5507950Z 118 |     print(f"  [OK] Memory estimation triggered {flush_count[0]} auto-flushes for 20 docs with {limit} byte limit")
2026-01-26T14:33:47.5508015Z     |
2026-01-26T14:33:47.5508100Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5508105Z 
2026-01-26T14:33:47.5508185Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5508269Z    --> test_memory_limits.py:124:1
2026-01-26T14:33:47.5508328Z     |
2026-01-26T14:33:47.5508474Z 122 |     """Test that flushing empty buffer doesn't call callback"""
2026-01-26T14:33:47.5508568Z 123 |     print("Testing empty flush...")
2026-01-26T14:33:47.5508628Z 124 |     
2026-01-26T14:33:47.5508686Z     | ^^^^
2026-01-26T14:33:47.5508761Z 125 |     call_count = [0]
2026-01-26T14:33:47.5508926Z     |
2026-01-26T14:33:47.5509012Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5509016Z 
2026-01-26T14:33:47.5509096Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5509180Z    --> test_memory_limits.py:126:1
2026-01-26T14:33:47.5509242Z     |
2026-01-26T14:33:47.5509312Z 125 |     call_count = [0]
2026-01-26T14:33:47.5509371Z 126 |     
2026-01-26T14:33:47.5509438Z     | ^^^^
2026-01-26T14:33:47.5509545Z 127 |     def count_calls(documents, metadatas, ids):
2026-01-26T14:33:47.5509618Z 128 |         call_count[0] += 1
2026-01-26T14:33:47.5509681Z     |
2026-01-26T14:33:47.5509766Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5509771Z 
2026-01-26T14:33:47.5509857Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5509938Z    --> test_memory_limits.py:129:1
2026-01-26T14:33:47.5509996Z     |
2026-01-26T14:33:47.5510099Z 127 |     def count_calls(documents, metadatas, ids):
2026-01-26T14:33:47.5510174Z 128 |         call_count[0] += 1
2026-01-26T14:33:47.5510237Z 129 |     
2026-01-26T14:33:47.5510296Z     | ^^^^
2026-01-26T14:33:47.5510421Z 130 |     indexer = MemoryLimitedIndexer(1024, count_calls)
2026-01-26T14:33:47.5510484Z     |
2026-01-26T14:33:47.5510571Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5510576Z 
2026-01-26T14:33:47.5510657Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5510737Z    --> test_memory_limits.py:131:1
2026-01-26T14:33:47.5510802Z     |
2026-01-26T14:33:47.5510921Z 130 |     indexer = MemoryLimitedIndexer(1024, count_calls)
2026-01-26T14:33:47.5510980Z 131 |     
2026-01-26T14:33:47.5511043Z     | ^^^^
2026-01-26T14:33:47.5511113Z 132 |     indexer.flush()
2026-01-26T14:33:47.5511189Z 133 |     assert call_count[0] == 0
2026-01-26T14:33:47.5511252Z     |
2026-01-26T14:33:47.5511342Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5511346Z 
2026-01-26T14:33:47.5511528Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5511661Z    --> test_memory_limits.py:134:1
2026-01-26T14:33:47.5511759Z     |
2026-01-26T14:33:47.5511871Z 132 |     indexer.flush()
2026-01-26T14:33:47.5511998Z 133 |     assert call_count[0] == 0
2026-01-26T14:33:47.5512115Z 134 |     
2026-01-26T14:33:47.5512206Z     | ^^^^
2026-01-26T14:33:47.5512438Z 135 |     indexer.add_chunk("test", {"source": "file.py"}, "id_0")
2026-01-26T14:33:47.5512553Z 136 |     indexer.flush()
2026-01-26T14:33:47.5512652Z     |
2026-01-26T14:33:47.5512780Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5512788Z 
2026-01-26T14:33:47.5512914Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5513045Z    --> test_memory_limits.py:138:1
2026-01-26T14:33:47.5513139Z     |
2026-01-26T14:33:47.5513246Z 136 |     indexer.flush()
2026-01-26T14:33:47.5513588Z 137 |     assert call_count[0] == 1
2026-01-26T14:33:47.5513690Z 138 |     
2026-01-26T14:33:47.5513783Z     | ^^^^
2026-01-26T14:33:47.5513891Z 139 |     indexer.flush()
2026-01-26T14:33:47.5514167Z 140 |     assert call_count[0] == 1
2026-01-26T14:33:47.5514266Z     |
2026-01-26T14:33:47.5514405Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5514414Z 
2026-01-26T14:33:47.5514559Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5514686Z    --> test_memory_limits.py:141:1
2026-01-26T14:33:47.5514780Z     |
2026-01-26T14:33:47.5514894Z 139 |     indexer.flush()
2026-01-26T14:33:47.5515031Z 140 |     assert call_count[0] == 1
2026-01-26T14:33:47.5515121Z 141 |     
2026-01-26T14:33:47.5515208Z     | ^^^^
2026-01-26T14:33:47.5515396Z 142 |     print("  [OK] Empty flush doesn't call callback")
2026-01-26T14:33:47.5515492Z     |
2026-01-26T14:33:47.5515640Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5515648Z 
2026-01-26T14:33:47.5515799Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5515945Z    --> test_memory_limits.py:148:1
2026-01-26T14:33:47.5516045Z     |
2026-01-26T14:33:47.5516248Z 146 |     """Test that metadata is correctly preserved"""
2026-01-26T14:33:47.5516436Z 147 |     print("Testing metadata preservation...")
2026-01-26T14:33:47.5516532Z 148 |     
2026-01-26T14:33:47.5516624Z     | ^^^^
2026-01-26T14:33:47.5516740Z 149 |     collected = []
2026-01-26T14:33:47.5516837Z     |
2026-01-26T14:33:47.5516984Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5516992Z 
2026-01-26T14:33:47.5517130Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5517269Z    --> test_memory_limits.py:150:1
2026-01-26T14:33:47.5517366Z     |
2026-01-26T14:33:47.5517478Z 149 |     collected = []
2026-01-26T14:33:47.5517583Z 150 |     
2026-01-26T14:33:47.5517686Z     | ^^^^
2026-01-26T14:33:47.5517845Z 151 |     def collect(documents, metadatas, ids):
2026-01-26T14:33:47.5518131Z 152 |         collected.append((documents.copy(), metadatas.copy(), ids.copy()))
2026-01-26T14:33:47.5518252Z     |
2026-01-26T14:33:47.5518410Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5518419Z 
2026-01-26T14:33:47.5518559Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5518705Z    --> test_memory_limits.py:153:1
2026-01-26T14:33:47.5518979Z     |
2026-01-26T14:33:47.5519163Z 151 |     def collect(documents, metadatas, ids):
2026-01-26T14:33:47.5519473Z 152 |         collected.append((documents.copy(), metadatas.copy(), ids.copy()))
2026-01-26T14:33:47.5519585Z 153 |     
2026-01-26T14:33:47.5519692Z     | ^^^^
2026-01-26T14:33:47.5519931Z 154 |     indexer = MemoryLimitedIndexer(10 * 1024 * 1024, collect)
2026-01-26T14:33:47.5520035Z     |
2026-01-26T14:33:47.5520179Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5520186Z 
2026-01-26T14:33:47.5520324Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5520460Z    --> test_memory_limits.py:155:1
2026-01-26T14:33:47.5520521Z     |
2026-01-26T14:33:47.5520664Z 154 |     indexer = MemoryLimitedIndexer(10 * 1024 * 1024, collect)
2026-01-26T14:33:47.5520729Z 155 |     
2026-01-26T14:33:47.5520788Z     | ^^^^
2026-01-26T14:33:47.5520854Z 156 |     test_data = [
2026-01-26T14:33:47.5521002Z 157 |         ("doc1", {"source": "file1.py", "chunk_index": 0}, "file1_0"),
2026-01-26T14:33:47.5521065Z     |
2026-01-26T14:33:47.5521166Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5521171Z 
2026-01-26T14:33:47.5521250Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5521333Z    --> test_memory_limits.py:161:1
2026-01-26T14:33:47.5521389Z     |
2026-01-26T14:33:47.5521522Z 159 |         ("doc3", {"source": "file2.py", "chunk_index": 0}, "file2_0"),
2026-01-26T14:33:47.5521583Z 160 |     ]
2026-01-26T14:33:47.5521648Z 161 |     
2026-01-26T14:33:47.5521706Z     | ^^^^
2026-01-26T14:33:47.5521797Z 162 |     for doc, meta, doc_id in test_data:
2026-01-26T14:33:47.5521898Z 163 |         indexer.add_chunk(doc, meta, doc_id)
2026-01-26T14:33:47.5522126Z     |
2026-01-26T14:33:47.5522213Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5522218Z 
2026-01-26T14:33:47.5522303Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5522381Z    --> test_memory_limits.py:164:1
2026-01-26T14:33:47.5522537Z     |
2026-01-26T14:33:47.5522628Z 162 |     for doc, meta, doc_id in test_data:
2026-01-26T14:33:47.5522725Z 163 |         indexer.add_chunk(doc, meta, doc_id)
2026-01-26T14:33:47.5522786Z 164 |     
2026-01-26T14:33:47.5522844Z     | ^^^^
2026-01-26T14:33:47.5522924Z 165 |     indexer.flush()
2026-01-26T14:33:47.5522984Z     |
2026-01-26T14:33:47.5523068Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5523072Z 
2026-01-26T14:33:47.5523151Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5523234Z    --> test_memory_limits.py:166:1
2026-01-26T14:33:47.5523293Z     |
2026-01-26T14:33:47.5523362Z 165 |     indexer.flush()
2026-01-26T14:33:47.5523425Z 166 |     
2026-01-26T14:33:47.5523484Z     | ^^^^
2026-01-26T14:33:47.5523566Z 167 |     assert len(collected) == 1
2026-01-26T14:33:47.5523650Z 168 |     docs, metas, ids = collected[0]
2026-01-26T14:33:47.5523714Z     |
2026-01-26T14:33:47.5523796Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5523800Z 
2026-01-26T14:33:47.5523884Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5523969Z    --> test_memory_limits.py:169:1
2026-01-26T14:33:47.5524026Z     |
2026-01-26T14:33:47.5524103Z 167 |     assert len(collected) == 1
2026-01-26T14:33:47.5524190Z 168 |     docs, metas, ids = collected[0]
2026-01-26T14:33:47.5524249Z 169 |     
2026-01-26T14:33:47.5524305Z     | ^^^^
2026-01-26T14:33:47.5524396Z 170 |     assert docs == ["doc1", "doc2", "doc3"]
2026-01-26T14:33:47.5524515Z 171 |     assert ids == ["file1_0", "file1_1", "file2_0"]
2026-01-26T14:33:47.5524573Z     |
2026-01-26T14:33:47.5524658Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5524662Z 
2026-01-26T14:33:47.5524748Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5524829Z    --> test_memory_limits.py:175:1
2026-01-26T14:33:47.5524886Z     |
2026-01-26T14:33:47.5525035Z 173 |     assert metas[1] == {"source": "file1.py", "chunk_index": 1}
2026-01-26T14:33:47.5525171Z 174 |     assert metas[2] == {"source": "file2.py", "chunk_index": 0}
2026-01-26T14:33:47.5525230Z 175 |     
2026-01-26T14:33:47.5525288Z     | ^^^^
2026-01-26T14:33:47.5525406Z 176 |     print("  [OK] Metadata preserved correctly")
2026-01-26T14:33:47.5525465Z     |
2026-01-26T14:33:47.5525550Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5525554Z 
2026-01-26T14:33:47.5525639Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5525716Z    --> test_memory_limits.py:182:1
2026-01-26T14:33:47.5525774Z     |
2026-01-26T14:33:47.5525882Z 180 |     """Test that buffer is cleared after flush"""
2026-01-26T14:33:47.5525984Z 181 |     print("Testing buffer clearing...")
2026-01-26T14:33:47.5526042Z 182 |     
2026-01-26T14:33:47.5526100Z     | ^^^^
2026-01-26T14:33:47.5526271Z 183 |     indexer = MemoryLimitedIndexer(1024 * 1024, lambda d, m, i: None)
2026-01-26T14:33:47.5526329Z     |
2026-01-26T14:33:47.5526413Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5526417Z 
2026-01-26T14:33:47.5526506Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5526583Z    --> test_memory_limits.py:184:1
2026-01-26T14:33:47.5526640Z     |
2026-01-26T14:33:47.5526794Z 183 |     indexer = MemoryLimitedIndexer(1024 * 1024, lambda d, m, i: None)
2026-01-26T14:33:47.5526857Z 184 |     
2026-01-26T14:33:47.5526916Z     | ^^^^
2026-01-26T14:33:47.5527052Z 185 |     indexer.add_chunk("doc1", {"source": "file.py"}, "id1")
2026-01-26T14:33:47.5527186Z 186 |     indexer.add_chunk("doc2", {"source": "file.py"}, "id2")
2026-01-26T14:33:47.5527244Z     |
2026-01-26T14:33:47.5527327Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5527332Z 
2026-01-26T14:33:47.5527417Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5527494Z    --> test_memory_limits.py:187:1
2026-01-26T14:33:47.5527686Z     |
2026-01-26T14:33:47.5527815Z 185 |     indexer.add_chunk("doc1", {"source": "file.py"}, "id1")
2026-01-26T14:33:47.5527947Z 186 |     indexer.add_chunk("doc2", {"source": "file.py"}, "id2")
2026-01-26T14:33:47.5528005Z 187 |     
2026-01-26T14:33:47.5528132Z     | ^^^^
2026-01-26T14:33:47.5528228Z 188 |     stats_before = indexer.get_stats()
2026-01-26T14:33:47.5528352Z 189 |     assert stats_before["current_buffer_chunks"] == 2
2026-01-26T14:33:47.5528413Z     |
2026-01-26T14:33:47.5528497Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5528507Z 
2026-01-26T14:33:47.5528586Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5528663Z    --> test_memory_limits.py:191:1
2026-01-26T14:33:47.5528720Z     |
2026-01-26T14:33:47.5529097Z 189 |     assert stats_before["current_buffer_chunks"] == 2
2026-01-26T14:33:47.5529221Z 190 |     assert stats_before["current_buffer_bytes"] > 0
2026-01-26T14:33:47.5529282Z 191 |     
2026-01-26T14:33:47.5529345Z     | ^^^^
2026-01-26T14:33:47.5529421Z 192 |     indexer.flush()
2026-01-26T14:33:47.5529478Z     |
2026-01-26T14:33:47.5529562Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5529568Z 
2026-01-26T14:33:47.5529654Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5529734Z    --> test_memory_limits.py:193:1
2026-01-26T14:33:47.5529792Z     |
2026-01-26T14:33:47.5529873Z 192 |     indexer.flush()
2026-01-26T14:33:47.5529935Z 193 |     
2026-01-26T14:33:47.5529993Z     | ^^^^
2026-01-26T14:33:47.5530083Z 194 |     stats_after = indexer.get_stats()
2026-01-26T14:33:47.5530207Z 195 |     assert stats_after["current_buffer_chunks"] == 0
2026-01-26T14:33:47.5530264Z     |
2026-01-26T14:33:47.5530348Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5530353Z 
2026-01-26T14:33:47.5530437Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5530513Z    --> test_memory_limits.py:198:1
2026-01-26T14:33:47.5530570Z     |
2026-01-26T14:33:47.5530684Z 196 |     assert stats_after["current_buffer_bytes"] == 0
2026-01-26T14:33:47.5530783Z 197 |     assert stats_after["total_chunks"] == 2
2026-01-26T14:33:47.5530842Z 198 |     
2026-01-26T14:33:47.5530898Z     | ^^^^
2026-01-26T14:33:47.5531008Z 199 |     print("  [OK] Buffer cleared after flush")
2026-01-26T14:33:47.5531072Z     |
2026-01-26T14:33:47.5531159Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5531164Z 
2026-01-26T14:33:47.5531252Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5531330Z    --> test_memory_limits.py:207:1
2026-01-26T14:33:47.5531389Z     |
2026-01-26T14:33:47.5531463Z 205 |     print("=" * 50)
2026-01-26T14:33:47.5531529Z 206 |     print()
2026-01-26T14:33:47.5531587Z 207 |     
2026-01-26T14:33:47.5531644Z     | ^^^^
2026-01-26T14:33:47.5531709Z 208 |     try:
2026-01-26T14:33:47.5531788Z 209 |         test_basic_indexing()
2026-01-26T14:33:47.5531846Z     |
2026-01-26T14:33:47.5531935Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5531940Z 
2026-01-26T14:33:47.5532018Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5532098Z    --> test_memory_limits.py:216:1
2026-01-26T14:33:47.5532156Z     |
2026-01-26T14:33:47.5532249Z 214 |         test_metadata_preservation()
2026-01-26T14:33:47.5532325Z 215 |         test_buffer_clearing()
2026-01-26T14:33:47.5532387Z 216 |         
2026-01-26T14:33:47.5532452Z     | ^^^^^^^^
2026-01-26T14:33:47.5532516Z 217 |         print()
2026-01-26T14:33:47.5532586Z 218 |         print("=" * 50)
2026-01-26T14:33:47.5532643Z     |
2026-01-26T14:33:47.5532745Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5532750Z 
2026-01-26T14:33:47.5532855Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5532942Z  --> test_path_validation.py:2:1
2026-01-26T14:33:47.5533008Z   |
2026-01-26T14:33:47.5533118Z 1 |   """Tests for path validation security feature"""
2026-01-26T14:33:47.5533183Z 2 | / import sys
2026-01-26T14:33:47.5533251Z 3 | | import os
2026-01-26T14:33:47.5533333Z 4 | | from pathlib import Path
2026-01-26T14:33:47.5533527Z   | |________________________^
2026-01-26T14:33:47.5533586Z 5 |
2026-01-26T14:33:47.5533671Z 6 |   sys.path.append(os.getcwd())
2026-01-26T14:33:47.5533729Z   |
2026-01-26T14:33:47.5533802Z help: Organize imports
2026-01-26T14:33:47.5533807Z 
2026-01-26T14:33:47.5534008Z F401 [*] `pathlib.Path` imported but unused
2026-01-26T14:33:47.5534096Z  --> test_path_validation.py:4:21
2026-01-26T14:33:47.5534154Z   |
2026-01-26T14:33:47.5534217Z 2 | import sys
2026-01-26T14:33:47.5534284Z 3 | import os
2026-01-26T14:33:47.5534361Z 4 | from pathlib import Path
2026-01-26T14:33:47.5534426Z   |                     ^^^^
2026-01-26T14:33:47.5534488Z 5 |
2026-01-26T14:33:47.5534568Z 6 | sys.path.append(os.getcwd())
2026-01-26T14:33:47.5534625Z   |
2026-01-26T14:33:47.5534720Z help: Remove unused import: `pathlib.Path`
2026-01-26T14:33:47.5534726Z 
2026-01-26T14:33:47.5534832Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5534911Z  --> test_path_validation.py:8:1
2026-01-26T14:33:47.5534972Z   |
2026-01-26T14:33:47.5535056Z 6 | sys.path.append(os.getcwd())
2026-01-26T14:33:47.5535113Z 7 |
2026-01-26T14:33:47.5535219Z 8 | from config import validate_path, PROJECT_ROOT
2026-01-26T14:33:47.5535298Z   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5535367Z   |
2026-01-26T14:33:47.5535437Z help: Organize imports
2026-01-26T14:33:47.5535442Z 
2026-01-26T14:33:47.5535526Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5535613Z   --> test_path_validation.py:14:1
2026-01-26T14:33:47.5535670Z    |
2026-01-26T14:33:47.5535808Z 12 |     """Test that valid paths within project are accepted"""
2026-01-26T14:33:47.5535901Z 13 |     print("Testing valid paths...")
2026-01-26T14:33:47.5535960Z 14 |     
2026-01-26T14:33:47.5536017Z    | ^^^^
2026-01-26T14:33:47.5536095Z 15 |     valid = validate_path(".")
2026-01-26T14:33:47.5536180Z 16 |     assert valid == PROJECT_ROOT
2026-01-26T14:33:47.5536238Z    |
2026-01-26T14:33:47.5536323Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5536331Z 
2026-01-26T14:33:47.5536417Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5536497Z   --> test_path_validation.py:18:1
2026-01-26T14:33:47.5536555Z    |
2026-01-26T14:33:47.5536638Z 16 |     assert valid == PROJECT_ROOT
2026-01-26T14:33:47.5536746Z 17 |     print("  [OK] Current directory validated")
2026-01-26T14:33:47.5536805Z 18 |     
2026-01-26T14:33:47.5536862Z    | ^^^^
2026-01-26T14:33:47.5536955Z 19 |     valid = validate_path("config.py")
2026-01-26T14:33:47.5537056Z 20 |     assert valid == PROJECT_ROOT / "config.py"
2026-01-26T14:33:47.5537115Z    |
2026-01-26T14:33:47.5537203Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5537208Z 
2026-01-26T14:33:47.5537287Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5537369Z   --> test_path_validation.py:22:1
2026-01-26T14:33:47.5537426Z    |
2026-01-26T14:33:47.5537530Z 20 |     assert valid == PROJECT_ROOT / "config.py"
2026-01-26T14:33:47.5537624Z 21 |     print("  [OK] File in root validated")
2026-01-26T14:33:47.5537687Z 22 |     
2026-01-26T14:33:47.5537750Z    | ^^^^
2026-01-26T14:33:47.5537828Z 23 |     valid = validate_path(".ai")
2026-01-26T14:33:47.5537917Z 24 |     assert valid == PROJECT_ROOT / ".ai"
2026-01-26T14:33:47.5537975Z    |
2026-01-26T14:33:47.5538070Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5538075Z 
2026-01-26T14:33:47.5538155Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5538234Z   --> test_path_validation.py:26:1
2026-01-26T14:33:47.5538297Z    |
2026-01-26T14:33:47.5538383Z 24 |     assert valid == PROJECT_ROOT / ".ai"
2026-01-26T14:33:47.5538481Z 25 |     print("  [OK] Hidden directory validated")
2026-01-26T14:33:47.5538545Z 26 |     
2026-01-26T14:33:47.5538602Z    | ^^^^
2026-01-26T14:33:47.5538704Z 27 |     print("[PASS] Valid paths test passed\n")
2026-01-26T14:33:47.5538865Z    |
2026-01-26T14:33:47.5538961Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5538966Z 
2026-01-26T14:33:47.5539046Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5539249Z   --> test_path_validation.py:33:1
2026-01-26T14:33:47.5539314Z    |
2026-01-26T14:33:47.5539430Z 31 |     """Test that paths outside project are rejected"""
2026-01-26T14:33:47.5539617Z 32 |     print("Testing invalid paths...")
2026-01-26T14:33:47.5539683Z 33 |     
2026-01-26T14:33:47.5539742Z    | ^^^^
2026-01-26T14:33:47.5539810Z 34 |     test_cases = [
2026-01-26T14:33:47.5539932Z 35 |         ("../../etc/passwd", "Parent directory traversal"),
2026-01-26T14:33:47.5539993Z    |
2026-01-26T14:33:47.5540076Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5540081Z 
2026-01-26T14:33:47.5540161Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5540246Z   --> test_path_validation.py:40:1
2026-01-26T14:33:47.5540306Z    |
2026-01-26T14:33:47.5540378Z 38 |         ("", "Empty path"),
2026-01-26T14:33:47.5540437Z 39 |     ]
2026-01-26T14:33:47.5540501Z 40 |     
2026-01-26T14:33:47.5540559Z    | ^^^^
2026-01-26T14:33:47.5540654Z 41 |     for path, description in test_cases:
2026-01-26T14:33:47.5540722Z 42 |         try:
2026-01-26T14:33:47.5540779Z    |
2026-01-26T14:33:47.5540863Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5540868Z 
2026-01-26T14:33:47.5540950Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5541034Z   --> test_path_validation.py:48:1
2026-01-26T14:33:47.5541091Z    |
2026-01-26T14:33:47.5541166Z 46 |         except ValueError:
2026-01-26T14:33:47.5541277Z 47 |             print(f"  [OK] Blocked: {description}")
2026-01-26T14:33:47.5541338Z 48 |     
2026-01-26T14:33:47.5541397Z    | ^^^^
2026-01-26T14:33:47.5541507Z 49 |     print("[PASS] Invalid paths test passed\n")
2026-01-26T14:33:47.5541568Z    |
2026-01-26T14:33:47.5541650Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5541655Z 
2026-01-26T14:33:47.5541735Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5541819Z   --> test_path_validation.py:55:1
2026-01-26T14:33:47.5541876Z    |
2026-01-26T14:33:47.5541952Z 53 |     """Test edge cases"""
2026-01-26T14:33:47.5542039Z 54 |     print("Testing edge cases...")
2026-01-26T14:33:47.5542097Z 55 |     
2026-01-26T14:33:47.5542155Z    | ^^^^
2026-01-26T14:33:47.5542224Z 56 |     try:
2026-01-26T14:33:47.5542305Z 57 |         validate_path(123)
2026-01-26T14:33:47.5542363Z    |
2026-01-26T14:33:47.5542448Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5542453Z 
2026-01-26T14:33:47.5542540Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5542618Z   --> test_path_validation.py:62:1
2026-01-26T14:33:47.5542675Z    |
2026-01-26T14:33:47.5542750Z 60 |     except ValueError:
2026-01-26T14:33:47.5542858Z 61 |         print("  [OK] Non-string path rejected")
2026-01-26T14:33:47.5542916Z 62 |     
2026-01-26T14:33:47.5542974Z    | ^^^^
2026-01-26T14:33:47.5543039Z 63 |     try:
2026-01-26T14:33:47.5543111Z 64 |         validate_path(None)
2026-01-26T14:33:47.5543168Z    |
2026-01-26T14:33:47.5543260Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5543268Z 
2026-01-26T14:33:47.5543349Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5543431Z   --> test_path_validation.py:69:1
2026-01-26T14:33:47.5543489Z    |
2026-01-26T14:33:47.5543582Z 67 |     except (ValueError, TypeError):
2026-01-26T14:33:47.5543675Z 68 |         print("  [OK] None path rejected")
2026-01-26T14:33:47.5543736Z 69 |     
2026-01-26T14:33:47.5543798Z    | ^^^^
2026-01-26T14:33:47.5543896Z 70 |     print("[PASS] Edge cases test passed\n")
2026-01-26T14:33:47.5543954Z    |
2026-01-26T14:33:47.5544037Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5544041Z 
2026-01-26T14:33:47.5544125Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5544205Z   --> test_path_validation.py:78:1
2026-01-26T14:33:47.5544263Z    |
2026-01-26T14:33:47.5544341Z 76 |     print("=" * 50)
2026-01-26T14:33:47.5544438Z 77 |     print(f"Project root: {PROJECT_ROOT}\n")
2026-01-26T14:33:47.5544497Z 78 |     
2026-01-26T14:33:47.5544559Z    | ^^^^
2026-01-26T14:33:47.5544709Z 79 |     try:
2026-01-26T14:33:47.5544782Z 80 |         test_valid_paths()
2026-01-26T14:33:47.5544841Z    |
2026-01-26T14:33:47.5544930Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5544935Z 
2026-01-26T14:33:47.5545110Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5545186Z  --> test_search.py:1:1
2026-01-26T14:33:47.5545249Z   |
2026-01-26T14:33:47.5545312Z 1 | / import os
2026-01-26T14:33:47.5545374Z 2 | | import sys
2026-01-26T14:33:47.5545434Z   | |__________^
2026-01-26T14:33:47.5545520Z 3 |   sys.path.append(os.getcwd())
2026-01-26T14:33:47.5545577Z   |
2026-01-26T14:33:47.5545649Z help: Organize imports
2026-01-26T14:33:47.5545654Z 
2026-01-26T14:33:47.5545759Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5545830Z  --> test_search.py:5:1
2026-01-26T14:33:47.5545887Z   |
2026-01-26T14:33:47.5545969Z 3 | sys.path.append(os.getcwd())
2026-01-26T14:33:47.5546031Z 4 |
2026-01-26T14:33:47.5546161Z 5 | from mcp_server import search_codebase, get_index_stats
2026-01-26T14:33:47.5546254Z   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5546317Z 6 |
2026-01-26T14:33:47.5546418Z 7 | print("Testing search functionality...")
2026-01-26T14:33:47.5546475Z   |
2026-01-26T14:33:47.5546548Z help: Organize imports
2026-01-26T14:33:47.5546569Z 
2026-01-26T14:33:47.5546667Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5546737Z  --> test_stdio.py:4:1
2026-01-26T14:33:47.5546795Z   |
2026-01-26T14:33:47.5546895Z 2 |   """Test MCP server stdio communication"""
2026-01-26T14:33:47.5546952Z 3 |
2026-01-26T14:33:47.5547021Z 4 | / import subprocess
2026-01-26T14:33:47.5547091Z 5 | | import json
2026-01-26T14:33:47.5547153Z 6 | | import sys
2026-01-26T14:33:47.5547225Z   | |__________^
2026-01-26T14:33:47.5547282Z 7 |
2026-01-26T14:33:47.5547361Z 8 |   def test_mcp_server():
2026-01-26T14:33:47.5547418Z   |
2026-01-26T14:33:47.5547487Z help: Organize imports
2026-01-26T14:33:47.5547491Z 
2026-01-26T14:33:47.5547581Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5547655Z   --> test_stdio.py:10:1
2026-01-26T14:33:47.5547713Z    |
2026-01-26T14:33:47.5547786Z  8 | def test_mcp_server():
2026-01-26T14:33:47.5547891Z  9 |     """Test basic MCP server communication"""
2026-01-26T14:33:47.5547950Z 10 |     
2026-01-26T14:33:47.5548007Z    | ^^^^
2026-01-26T14:33:47.5548080Z 11 |     # Start server
2026-01-26T14:33:47.5548164Z 12 |     process = subprocess.Popen(
2026-01-26T14:33:47.5548222Z    |
2026-01-26T14:33:47.5548306Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5548311Z 
2026-01-26T14:33:47.5548397Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5548469Z   --> test_stdio.py:20:1
2026-01-26T14:33:47.5548527Z    |
2026-01-26T14:33:47.5548595Z 18 |         bufsize=0
2026-01-26T14:33:47.5548655Z 19 |     )
2026-01-26T14:33:47.5548712Z 20 |     
2026-01-26T14:33:47.5548871Z    | ^^^^
2026-01-26T14:33:47.5548941Z 21 |     try:
2026-01-26T14:33:47.5549022Z 22 |         # Send initialize request
2026-01-26T14:33:47.5549089Z    |
2026-01-26T14:33:47.5549178Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5549183Z 
2026-01-26T14:33:47.5549261Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5549338Z   --> test_stdio.py:36:1
2026-01-26T14:33:47.5549401Z    |
2026-01-26T14:33:47.5549465Z 34 |             }
2026-01-26T14:33:47.5549524Z 35 |         }
2026-01-26T14:33:47.5549583Z 36 |         
2026-01-26T14:33:47.5549647Z    | ^^^^^^^^
2026-01-26T14:33:47.5549745Z 37 |         print("Sending initialize request...")
2026-01-26T14:33:47.5549872Z 38 |         request_str = json.dumps(initialize_request) + "\n"
2026-01-26T14:33:47.5549934Z    |
2026-01-26T14:33:47.5550018Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5550023Z 
2026-01-26T14:33:47.5550103Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5550173Z   --> test_stdio.py:41:1
2026-01-26T14:33:47.5550235Z    |
2026-01-26T14:33:47.5550328Z 39 |         process.stdin.write(request_str)
2026-01-26T14:33:47.5550546Z 40 |         process.stdin.flush()
2026-01-26T14:33:47.5550617Z 41 |         
2026-01-26T14:33:47.5550675Z    | ^^^^^^^^
2026-01-26T14:33:47.5550747Z 42 |         # Read response
2026-01-26T14:33:47.5550936Z 43 |         print("Waiting for response...")
2026-01-26T14:33:47.5551000Z    |
2026-01-26T14:33:47.5551082Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5551087Z 
2026-01-26T14:33:47.5551164Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5551244Z   --> test_stdio.py:46:1
2026-01-26T14:33:47.5551301Z    |
2026-01-26T14:33:47.5551414Z 44 |         response_line = process.stdout.readline()
2026-01-26T14:33:47.5551513Z 45 |         print(f"Response: {response_line}")
2026-01-26T14:33:47.5551571Z 46 |         
2026-01-26T14:33:47.5551629Z    | ^^^^^^^^
2026-01-26T14:33:47.5551702Z 47 |         if response_line:
2026-01-26T14:33:47.5551809Z 48 |             response = json.loads(response_line)
2026-01-26T14:33:47.5551867Z    |
2026-01-26T14:33:47.5551954Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5551959Z 
2026-01-26T14:33:47.5552044Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5552115Z   --> test_stdio.py:50:1
2026-01-26T14:33:47.5552182Z    |
2026-01-26T14:33:47.5552291Z 48 |             response = json.loads(response_line)
2026-01-26T14:33:47.5552450Z 49 |             print(f"Parsed response: {json.dumps(response, indent=2)}")
2026-01-26T14:33:47.5552510Z 50 |             
2026-01-26T14:33:47.5552569Z    | ^^^^^^^^^^^^
2026-01-26T14:33:47.5552657Z 51 |             if "result" in response:
2026-01-26T14:33:47.5553009Z 52 |                 print("\n✅ Server responded successfully!")
2026-01-26T14:33:47.5553069Z    |
2026-01-26T14:33:47.5553160Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5553165Z 
2026-01-26T14:33:47.5553247Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5553323Z   --> test_stdio.py:64:1
2026-01-26T14:33:47.5553381Z    |
2026-01-26T14:33:47.5553483Z 62 |                 print(f"Server stderr: {stderr}")
2026-01-26T14:33:47.5553562Z 63 |             return False
2026-01-26T14:33:47.5553623Z 64 |             
2026-01-26T14:33:47.5553690Z    | ^^^^^^^^^^^^
2026-01-26T14:33:47.5553765Z 65 |     except Exception as e:
2026-01-26T14:33:47.5553900Z 66 |         print(f"\n❌ Error: {e}")
2026-01-26T14:33:47.5553964Z    |
2026-01-26T14:33:47.5554049Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5554054Z 
2026-01-26T14:33:47.5554158Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5554244Z  --> test_transactional_save.py:1:1
2026-01-26T14:33:47.5554308Z   |
2026-01-26T14:33:47.5554372Z 1 | / import sys
2026-01-26T14:33:47.5554434Z 2 | | import os
2026-01-26T14:33:47.5554503Z 3 | | import json
2026-01-26T14:33:47.5554573Z 4 | | import tempfile
2026-01-26T14:33:47.5554640Z 5 | | import threading
2026-01-26T14:33:47.5554703Z 6 | | import time
2026-01-26T14:33:47.5554791Z 7 | | from pathlib import Path
2026-01-26T14:33:47.5554856Z   | |________________________^
2026-01-26T14:33:47.5554919Z 8 |
2026-01-26T14:33:47.5555004Z 9 |   sys.path.append(os.getcwd())
2026-01-26T14:33:47.5555061Z   |
2026-01-26T14:33:47.5555131Z help: Organize imports
2026-01-26T14:33:47.5555136Z 
2026-01-26T14:33:47.5555242Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5555338Z   --> test_transactional_save.py:11:1
2026-01-26T14:33:47.5555397Z    |
2026-01-26T14:33:47.5555479Z  9 |   sys.path.append(os.getcwd())
2026-01-26T14:33:47.5555543Z 10 |
2026-01-26T14:33:47.5555734Z 11 | / from incremental_indexing import IndexMetadata, atomic_write, file_lock
2026-01-26T14:33:47.5555827Z 12 | | from config import INDEX_METADATA_FILE
2026-01-26T14:33:47.5555908Z    | |______________________________________^
2026-01-26T14:33:47.5555966Z    |
2026-01-26T14:33:47.5556036Z help: Organize imports
2026-01-26T14:33:47.5556041Z 
2026-01-26T14:33:47.5556176Z F401 [*] `incremental_indexing.file_lock` imported but unused
2026-01-26T14:33:47.5556267Z   --> test_transactional_save.py:11:63
2026-01-26T14:33:47.5556416Z    |
2026-01-26T14:33:47.5556498Z  9 | sys.path.append(os.getcwd())
2026-01-26T14:33:47.5556560Z 10 |
2026-01-26T14:33:47.5556742Z 11 | from incremental_indexing import IndexMetadata, atomic_write, file_lock
2026-01-26T14:33:47.5556915Z    |                                                               ^^^^^^^^^
2026-01-26T14:33:47.5557015Z 12 | from config import INDEX_METADATA_FILE
2026-01-26T14:33:47.5557073Z    |
2026-01-26T14:33:47.5557215Z help: Remove unused import: `incremental_indexing.file_lock`
2026-01-26T14:33:47.5557220Z 
2026-01-26T14:33:47.5557303Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5557394Z   --> test_transactional_save.py:18:1
2026-01-26T14:33:47.5557455Z    |
2026-01-26T14:33:47.5557565Z 16 |     """Test atomic write creates file correctly"""
2026-01-26T14:33:47.5557657Z 17 |     print("Testing atomic write...")
2026-01-26T14:33:47.5557718Z 18 |     
2026-01-26T14:33:47.5557777Z    | ^^^^
2026-01-26T14:33:47.5557898Z 19 |     with tempfile.TemporaryDirectory() as tmpdir:
2026-01-26T14:33:47.5558006Z 20 |         test_file = Path(tmpdir) / "test.json"
2026-01-26T14:33:47.5558064Z    |
2026-01-26T14:33:47.5558154Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5558159Z 
2026-01-26T14:33:47.5558249Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5558333Z   --> test_transactional_save.py:22:1
2026-01-26T14:33:47.5558391Z    |
2026-01-26T14:33:47.5558490Z 20 |         test_file = Path(tmpdir) / "test.json"
2026-01-26T14:33:47.5558605Z 21 |         test_content = '{"test": "data", "number": 42}'
2026-01-26T14:33:47.5558666Z 22 |         
2026-01-26T14:33:47.5558725Z    | ^^^^^^^^
2026-01-26T14:33:47.5558939Z 23 |         atomic_write(test_file, test_content)
2026-01-26T14:33:47.5558999Z    |
2026-01-26T14:33:47.5559087Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5559092Z 
2026-01-26T14:33:47.5559180Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5559262Z   --> test_transactional_save.py:24:1
2026-01-26T14:33:47.5559324Z    |
2026-01-26T14:33:47.5559423Z 23 |         atomic_write(test_file, test_content)
2026-01-26T14:33:47.5559482Z 24 |         
2026-01-26T14:33:47.5559540Z    | ^^^^^^^^
2026-01-26T14:33:47.5559624Z 25 |         assert test_file.exists()
2026-01-26T14:33:47.5559743Z 26 |         content = test_file.read_text(encoding='utf-8')
2026-01-26T14:33:47.5559801Z    |
2026-01-26T14:33:47.5559884Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5559889Z 
2026-01-26T14:33:47.5559973Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5560055Z   --> test_transactional_save.py:28:1
2026-01-26T14:33:47.5560112Z    |
2026-01-26T14:33:47.5560221Z 26 |         content = test_file.read_text(encoding='utf-8')
2026-01-26T14:33:47.5560308Z 27 |         assert content == test_content
2026-01-26T14:33:47.5560366Z 28 |         
2026-01-26T14:33:47.5560425Z    | ^^^^^^^^
2026-01-26T14:33:47.5560511Z 29 |         data = json.loads(content)
2026-01-26T14:33:47.5560595Z 30 |         assert data["test"] == "data"
2026-01-26T14:33:47.5560656Z    |
2026-01-26T14:33:47.5560741Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5560750Z 
2026-01-26T14:33:47.5560829Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5560913Z   --> test_transactional_save.py:32:1
2026-01-26T14:33:47.5560970Z    |
2026-01-26T14:33:47.5561056Z 30 |         assert data["test"] == "data"
2026-01-26T14:33:47.5561136Z 31 |         assert data["number"] == 42
2026-01-26T14:33:47.5561195Z 32 |         
2026-01-26T14:33:47.5561258Z    | ^^^^^^^^
2026-01-26T14:33:47.5561381Z 33 |         print("  [OK] Atomic write creates file correctly")
2026-01-26T14:33:47.5561440Z    |
2026-01-26T14:33:47.5561524Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5561528Z 
2026-01-26T14:33:47.5561612Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5561694Z   --> test_transactional_save.py:39:1
2026-01-26T14:33:47.5561751Z    |
2026-01-26T14:33:47.5561870Z 37 |     """Test atomic write overwrites existing file"""
2026-01-26T14:33:47.5562099Z 38 |     print("Testing atomic write overwrite...")
2026-01-26T14:33:47.5562158Z 39 |     
2026-01-26T14:33:47.5562226Z    | ^^^^
2026-01-26T14:33:47.5562343Z 40 |     with tempfile.TemporaryDirectory() as tmpdir:
2026-01-26T14:33:47.5562533Z 41 |         test_file = Path(tmpdir) / "test.json"
2026-01-26T14:33:47.5562594Z    |
2026-01-26T14:33:47.5562685Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5562691Z 
2026-01-26T14:33:47.5562771Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5562852Z   --> test_transactional_save.py:42:1
2026-01-26T14:33:47.5562915Z    |
2026-01-26T14:33:47.5563027Z 40 |     with tempfile.TemporaryDirectory() as tmpdir:
2026-01-26T14:33:47.5563119Z 41 |         test_file = Path(tmpdir) / "test.json"
2026-01-26T14:33:47.5563178Z 42 |         
2026-01-26T14:33:47.5563242Z    | ^^^^^^^^
2026-01-26T14:33:47.5563333Z 43 |         test_file.write_text("old content")
2026-01-26T14:33:47.5563441Z 44 |         assert test_file.read_text() == "old content"
2026-01-26T14:33:47.5563508Z    |
2026-01-26T14:33:47.5563594Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5563599Z 
2026-01-26T14:33:47.5563679Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5563768Z   --> test_transactional_save.py:45:1
2026-01-26T14:33:47.5563825Z    |
2026-01-26T14:33:47.5563913Z 43 |         test_file.write_text("old content")
2026-01-26T14:33:47.5564020Z 44 |         assert test_file.read_text() == "old content"
2026-01-26T14:33:47.5564084Z 45 |         
2026-01-26T14:33:47.5564142Z    | ^^^^^^^^
2026-01-26T14:33:47.5564230Z 46 |         new_content = "new content"
2026-01-26T14:33:47.5564331Z 47 |         atomic_write(test_file, new_content)
2026-01-26T14:33:47.5564388Z    |
2026-01-26T14:33:47.5564476Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5564481Z 
2026-01-26T14:33:47.5564567Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5564662Z   --> test_transactional_save.py:48:1
2026-01-26T14:33:47.5564723Z    |
2026-01-26T14:33:47.5564801Z 46 |         new_content = "new content"
2026-01-26T14:33:47.5564904Z 47 |         atomic_write(test_file, new_content)
2026-01-26T14:33:47.5564973Z 48 |         
2026-01-26T14:33:47.5565031Z    | ^^^^^^^^
2026-01-26T14:33:47.5565160Z 49 |         assert test_file.read_text() == new_content
2026-01-26T14:33:47.5565289Z 50 |         print("  [OK] Atomic write overwrites correctly")
2026-01-26T14:33:47.5565354Z    |
2026-01-26T14:33:47.5565439Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5565444Z 
2026-01-26T14:33:47.5565531Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5565612Z   --> test_transactional_save.py:56:1
2026-01-26T14:33:47.5565669Z    |
2026-01-26T14:33:47.5565812Z 54 |     """Test that atomic write cleans up temp files on error"""
2026-01-26T14:33:47.5565927Z 55 |     print("Testing atomic write error cleanup...")
2026-01-26T14:33:47.5565985Z 56 |     
2026-01-26T14:33:47.5566051Z    | ^^^^
2026-01-26T14:33:47.5566169Z 57 |     with tempfile.TemporaryDirectory() as tmpdir:
2026-01-26T14:33:47.5566262Z 58 |         test_file = Path(tmpdir) / "test.json"
2026-01-26T14:33:47.5566319Z    |
2026-01-26T14:33:47.5566413Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5566421Z 
2026-01-26T14:33:47.5566578Z F841 Local variable `original_exists` is assigned to but never used
2026-01-26T14:33:47.5566660Z   --> test_transactional_save.py:61:9
2026-01-26T14:33:47.5566724Z    |
2026-01-26T14:33:47.5566825Z 59 |         original_content = '{"original": true}'
2026-01-26T14:33:47.5566919Z 60 |         test_file.write_text(original_content)
2026-01-26T14:33:47.5567016Z 61 |         original_exists = test_file.exists()
2026-01-26T14:33:47.5567086Z    |         ^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5567147Z 62 |         
2026-01-26T14:33:47.5567241Z 63 |         from unittest.mock import patch
2026-01-26T14:33:47.5567304Z    |
2026-01-26T14:33:47.5567445Z help: Remove assignment to unused variable `original_exists`
2026-01-26T14:33:47.5567534Z 
2026-01-26T14:33:47.5567616Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5567703Z   --> test_transactional_save.py:62:1
2026-01-26T14:33:47.5567761Z    |
2026-01-26T14:33:47.5568015Z 60 |         test_file.write_text(original_content)
2026-01-26T14:33:47.5568112Z 61 |         original_exists = test_file.exists()
2026-01-26T14:33:47.5568177Z 62 |         
2026-01-26T14:33:47.5568237Z    | ^^^^^^^^
2026-01-26T14:33:47.5568327Z 63 |         from unittest.mock import patch
2026-01-26T14:33:47.5568416Z 64 |         import incremental_indexing
2026-01-26T14:33:47.5568474Z    |
2026-01-26T14:33:47.5568562Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5568567Z 
2026-01-26T14:33:47.5568673Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5568754Z   --> test_transactional_save.py:63:9
2026-01-26T14:33:47.5568910Z    |
2026-01-26T14:33:47.5569004Z 61 |           original_exists = test_file.exists()
2026-01-26T14:33:47.5569069Z 62 |           
2026-01-26T14:33:47.5569165Z 63 | /         from unittest.mock import patch
2026-01-26T14:33:47.5569251Z 64 | |         import incremental_indexing
2026-01-26T14:33:47.5569327Z    | |___________________________________^
2026-01-26T14:33:47.5569387Z 65 |           
2026-01-26T14:33:47.5569696Z 66 |           with patch.object(incremental_indexing.os, 'replace', side_effect=OSError("Simulated replace failure")):
2026-01-26T14:33:47.5569759Z    |
2026-01-26T14:33:47.5569832Z help: Organize imports
2026-01-26T14:33:47.5569837Z 
2026-01-26T14:33:47.5569918Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5570000Z   --> test_transactional_save.py:65:1
2026-01-26T14:33:47.5570065Z    |
2026-01-26T14:33:47.5570152Z 63 |         from unittest.mock import patch
2026-01-26T14:33:47.5570235Z 64 |         import incremental_indexing
2026-01-26T14:33:47.5570299Z 65 |         
2026-01-26T14:33:47.5570357Z    | ^^^^^^^^
2026-01-26T14:33:47.5570649Z 66 |         with patch.object(incremental_indexing.os, 'replace', side_effect=OSError("Simulated replace failure")):
2026-01-26T14:33:47.5570730Z 67 |             try:
2026-01-26T14:33:47.5570814Z    |
2026-01-26T14:33:47.5570899Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5570904Z 
2026-01-26T14:33:47.5570988Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5571076Z   --> test_transactional_save.py:73:1
2026-01-26T14:33:47.5571133Z    |
2026-01-26T14:33:47.5571208Z 71 |             except OSError as e:
2026-01-26T14:33:47.5571334Z 72 |                 assert "Simulated replace failure" in str(e)
2026-01-26T14:33:47.5571393Z 73 |         
2026-01-26T14:33:47.5571452Z    | ^^^^^^^^
2026-01-26T14:33:47.5571530Z 74 |         if test_file.exists():
2026-01-26T14:33:47.5571661Z 75 |             assert test_file.read_text() == original_content
2026-01-26T14:33:47.5571718Z    |
2026-01-26T14:33:47.5571804Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5571809Z 
2026-01-26T14:33:47.5571906Z F541 [*] f-string without any placeholders
2026-01-26T14:33:47.5571994Z   --> test_transactional_save.py:77:19
2026-01-26T14:33:47.5572052Z    |
2026-01-26T14:33:47.5572175Z 75 |             assert test_file.read_text() == original_content
2026-01-26T14:33:47.5572237Z 76 |         else:
2026-01-26T14:33:47.5572410Z 77 |             print(f"  [WARNING] Original file was deleted (Windows behavior)")
2026-01-26T14:33:47.5572518Z    |                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5572583Z 78 |         
2026-01-26T14:33:47.5572699Z 79 |         temp_files = list(Path(tmpdir).glob(".*.tmp"))
2026-01-26T14:33:47.5572758Z    |
2026-01-26T14:33:47.5572849Z help: Remove extraneous `f` prefix
2026-01-26T14:33:47.5572854Z 
2026-01-26T14:33:47.5572939Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5573021Z   --> test_transactional_save.py:78:1
2026-01-26T14:33:47.5573084Z    |
2026-01-26T14:33:47.5573145Z 76 |         else:
2026-01-26T14:33:47.5573303Z 77 |             print(f"  [WARNING] Original file was deleted (Windows behavior)")
2026-01-26T14:33:47.5573486Z 78 |         
2026-01-26T14:33:47.5573550Z    | ^^^^^^^^
2026-01-26T14:33:47.5573659Z 79 |         temp_files = list(Path(tmpdir).glob(".*.tmp"))
2026-01-26T14:33:47.5573933Z 80 |         assert len(temp_files) == 0, f"Temp files not cleaned up: {temp_files}"
2026-01-26T14:33:47.5574000Z    |
2026-01-26T14:33:47.5574086Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5574091Z 
2026-01-26T14:33:47.5574171Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5574258Z   --> test_transactional_save.py:81:1
2026-01-26T14:33:47.5574315Z    |
2026-01-26T14:33:47.5574423Z 79 |         temp_files = list(Path(tmpdir).glob(".*.tmp"))
2026-01-26T14:33:47.5574586Z 80 |         assert len(temp_files) == 0, f"Temp files not cleaned up: {temp_files}"
2026-01-26T14:33:47.5574651Z 81 |         
2026-01-26T14:33:47.5574709Z    | ^^^^^^^^
2026-01-26T14:33:47.5574828Z 82 |         print("  [OK] Failed write cleans up temp files")
2026-01-26T14:33:47.5574896Z    |
2026-01-26T14:33:47.5574981Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5574986Z 
2026-01-26T14:33:47.5575067Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5575150Z   --> test_transactional_save.py:88:1
2026-01-26T14:33:47.5575217Z    |
2026-01-26T14:33:47.5575323Z 86 |     """Test IndexMetadata save and load cycle"""
2026-01-26T14:33:47.5575421Z 87 |     print("Testing metadata save/load...")
2026-01-26T14:33:47.5575485Z 88 |     
2026-01-26T14:33:47.5575542Z    | ^^^^
2026-01-26T14:33:47.5575623Z 89 |     metadata = IndexMetadata()
2026-01-26T14:33:47.5575686Z    |
2026-01-26T14:33:47.5575770Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5575775Z 
2026-01-26T14:33:47.5575855Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5575938Z   --> test_transactional_save.py:90:1
2026-01-26T14:33:47.5576004Z    |
2026-01-26T14:33:47.5576082Z 89 |     metadata = IndexMetadata()
2026-01-26T14:33:47.5576139Z 90 |     
2026-01-26T14:33:47.5576207Z    | ^^^^
2026-01-26T14:33:47.5576323Z 91 |     metadata.update_file("test_file.py", 1234567890.0)
2026-01-26T14:33:47.5576449Z 92 |     metadata.update_file("another_file.js", 9876543210.0)
2026-01-26T14:33:47.5576511Z    |
2026-01-26T14:33:47.5576605Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5576610Z 
2026-01-26T14:33:47.5576690Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5576774Z   --> test_transactional_save.py:93:1
2026-01-26T14:33:47.5576840Z    |
2026-01-26T14:33:47.5576951Z 91 |     metadata.update_file("test_file.py", 1234567890.0)
2026-01-26T14:33:47.5577072Z 92 |     metadata.update_file("another_file.js", 9876543210.0)
2026-01-26T14:33:47.5577135Z 93 |     
2026-01-26T14:33:47.5577195Z    | ^^^^
2026-01-26T14:33:47.5577267Z 94 |     metadata.save()
2026-01-26T14:33:47.5577325Z    |
2026-01-26T14:33:47.5577415Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5577420Z 
2026-01-26T14:33:47.5577499Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5577585Z   --> test_transactional_save.py:95:1
2026-01-26T14:33:47.5577649Z    |
2026-01-26T14:33:47.5577720Z 94 |     metadata.save()
2026-01-26T14:33:47.5577778Z 95 |     
2026-01-26T14:33:47.5577835Z    | ^^^^
2026-01-26T14:33:47.5577933Z 96 |     assert INDEX_METADATA_FILE.exists()
2026-01-26T14:33:47.5577990Z    |
2026-01-26T14:33:47.5578074Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5578079Z 
2026-01-26T14:33:47.5578167Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5578249Z   --> test_transactional_save.py:97:1
2026-01-26T14:33:47.5578319Z    |
2026-01-26T14:33:47.5578423Z 96 |     assert INDEX_METADATA_FILE.exists()
2026-01-26T14:33:47.5578485Z 97 |     
2026-01-26T14:33:47.5578541Z    | ^^^^
2026-01-26T14:33:47.5578622Z 98 |     new_metadata = IndexMetadata()
2026-01-26T14:33:47.5578685Z    |
2026-01-26T14:33:47.5578868Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5578874Z 
2026-01-26T14:33:47.5578956Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5579167Z    --> test_transactional_save.py:99:1
2026-01-26T14:33:47.5579228Z     |
2026-01-26T14:33:47.5579314Z  98 |     new_metadata = IndexMetadata()
2026-01-26T14:33:47.5579374Z  99 |     
2026-01-26T14:33:47.5579437Z     | ^^^^
2026-01-26T14:33:47.5579708Z 100 |     assert new_metadata.get_file_mtime("test_file.py") == 1234567890.0
2026-01-26T14:33:47.5579886Z 101 |     assert new_metadata.get_file_mtime("another_file.js") == 9876543210.0
2026-01-26T14:33:47.5579952Z     |
2026-01-26T14:33:47.5580035Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5580040Z 
2026-01-26T14:33:47.5580122Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5580210Z    --> test_transactional_save.py:102:1
2026-01-26T14:33:47.5580269Z     |
2026-01-26T14:33:47.5580429Z 100 |     assert new_metadata.get_file_mtime("test_file.py") == 1234567890.0
2026-01-26T14:33:47.5580596Z 101 |     assert new_metadata.get_file_mtime("another_file.js") == 9876543210.0
2026-01-26T14:33:47.5580661Z 102 |     
2026-01-26T14:33:47.5580724Z     | ^^^^
2026-01-26T14:33:47.5580849Z 103 |     print("  [OK] Metadata save/load works correctly")
2026-01-26T14:33:47.5580912Z     |
2026-01-26T14:33:47.5580995Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5581000Z 
2026-01-26T14:33:47.5581083Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5581175Z    --> test_transactional_save.py:109:1
2026-01-26T14:33:47.5581233Z     |
2026-01-26T14:33:47.5581355Z 107 |     """Test that concurrent writes don't corrupt file"""
2026-01-26T14:33:47.5581451Z 108 |     print("Testing concurrent writes...")
2026-01-26T14:33:47.5581514Z 109 |     
2026-01-26T14:33:47.5581572Z     | ^^^^
2026-01-26T14:33:47.5581697Z 110 |     with tempfile.TemporaryDirectory() as tmpdir:
2026-01-26T14:33:47.5581828Z 111 |         test_file = Path(tmpdir) / "concurrent.json"
2026-01-26T14:33:47.5581886Z     |
2026-01-26T14:33:47.5581975Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5581979Z 
2026-01-26T14:33:47.5582071Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5582160Z    --> test_transactional_save.py:114:1
2026-01-26T14:33:47.5582218Z     |
2026-01-26T14:33:47.5582287Z 112 |         results = []
2026-01-26T14:33:47.5582361Z 113 |         errors = []
2026-01-26T14:33:47.5582425Z 114 |         
2026-01-26T14:33:47.5582485Z     | ^^^^^^^^
2026-01-26T14:33:47.5582602Z 115 |         def write_worker(worker_id, iterations=5):
2026-01-26T14:33:47.5582677Z 116 |             success_count = 0
2026-01-26T14:33:47.5582735Z     |
2026-01-26T14:33:47.5582820Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5582825Z 
2026-01-26T14:33:47.5582912Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5582994Z    --> test_transactional_save.py:128:1
2026-01-26T14:33:47.5583052Z     |
2026-01-26T14:33:47.5583201Z 126 |                     errors.append((worker_id, type(e).__name__, str(e)))
2026-01-26T14:33:47.5583316Z 127 |             results.append((worker_id, success_count))
2026-01-26T14:33:47.5583380Z 128 |         
2026-01-26T14:33:47.5583439Z     | ^^^^^^^^
2026-01-26T14:33:47.5583515Z 129 |         threads = []
2026-01-26T14:33:47.5583595Z 130 |         for i in range(5):
2026-01-26T14:33:47.5583653Z     |
2026-01-26T14:33:47.5583752Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5583758Z 
2026-01-26T14:33:47.5583840Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5583922Z    --> test_transactional_save.py:134:1
2026-01-26T14:33:47.5583984Z     |
2026-01-26T14:33:47.5584058Z 132 |             threads.append(t)
2026-01-26T14:33:47.5584127Z 133 |             t.start()
2026-01-26T14:33:47.5584187Z 134 |         
2026-01-26T14:33:47.5584254Z     | ^^^^^^^^
2026-01-26T14:33:47.5584325Z 135 |         for t in threads:
2026-01-26T14:33:47.5584392Z 136 |             t.join()
2026-01-26T14:33:47.5584455Z     |
2026-01-26T14:33:47.5584539Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5584544Z 
2026-01-26T14:33:47.5584623Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5584793Z    --> test_transactional_save.py:137:1
2026-01-26T14:33:47.5584863Z     |
2026-01-26T14:33:47.5584932Z 135 |         for t in threads:
2026-01-26T14:33:47.5584998Z 136 |             t.join()
2026-01-26T14:33:47.5585062Z 137 |         
2026-01-26T14:33:47.5585194Z     | ^^^^^^^^
2026-01-26T14:33:47.5585262Z 138 |         if errors:
2026-01-26T14:33:47.5585485Z 139 |             unexpected_errors = [e for e in errors if "permission" not in str(e).lower()]
2026-01-26T14:33:47.5585543Z     |
2026-01-26T14:33:47.5585630Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5585635Z 
2026-01-26T14:33:47.5585714Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5585801Z    --> test_transactional_save.py:143:1
2026-01-26T14:33:47.5585859Z     |
2026-01-26T14:33:47.5586006Z 141 |                 print(f"  [FAIL] Unexpected errors: {unexpected_errors}")
2026-01-26T14:33:47.5586083Z 142 |                 sys.exit(1)
2026-01-26T14:33:47.5586142Z 143 |         
2026-01-26T14:33:47.5586205Z     | ^^^^^^^^
2026-01-26T14:33:47.5586340Z 144 |         total_successes = sum(count for _, count in results)
2026-01-26T14:33:47.5586403Z     |
2026-01-26T14:33:47.5586488Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5586493Z 
2026-01-26T14:33:47.5586574Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5586662Z    --> test_transactional_save.py:145:1
2026-01-26T14:33:47.5586720Z     |
2026-01-26T14:33:47.5586844Z 144 |         total_successes = sum(count for _, count in results)
2026-01-26T14:33:47.5586910Z 145 |         
2026-01-26T14:33:47.5586970Z     | ^^^^^^^^
2026-01-26T14:33:47.5587051Z 146 |         assert test_file.exists()
2026-01-26T14:33:47.5587173Z 147 |         content = test_file.read_text(encoding='utf-8')
2026-01-26T14:33:47.5587241Z     |
2026-01-26T14:33:47.5587322Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5587327Z 
2026-01-26T14:33:47.5587407Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5587495Z    --> test_transactional_save.py:151:1
2026-01-26T14:33:47.5587556Z     |
2026-01-26T14:33:47.5587633Z 149 |         assert "worker" in data
2026-01-26T14:33:47.5587720Z 150 |         assert "iteration" in data
2026-01-26T14:33:47.5587779Z 151 |         
2026-01-26T14:33:47.5587841Z     | ^^^^^^^^
2026-01-26T14:33:47.5588143Z 152 |         print(f"  [OK] Concurrent writes handled safely ({total_successes} successful writes, file not corrupted)")
2026-01-26T14:33:47.5588210Z     |
2026-01-26T14:33:47.5588294Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5588299Z 
2026-01-26T14:33:47.5588380Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5588467Z    --> test_transactional_save.py:158:1
2026-01-26T14:33:47.5588528Z     |
2026-01-26T14:33:47.5588638Z 156 |     """Test that temporary files are cleaned up"""
2026-01-26T14:33:47.5588740Z 157 |     print("Testing temp file cleanup...")
2026-01-26T14:33:47.5588905Z 158 |     
2026-01-26T14:33:47.5588965Z     | ^^^^
2026-01-26T14:33:47.5589085Z 159 |     with tempfile.TemporaryDirectory() as tmpdir:
2026-01-26T14:33:47.5589217Z 160 |         test_file = Path(tmpdir) / "cleanup_test.json"
2026-01-26T14:33:47.5589274Z     |
2026-01-26T14:33:47.5589358Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5589362Z 
2026-01-26T14:33:47.5589449Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5589534Z    --> test_transactional_save.py:161:1
2026-01-26T14:33:47.5589591Z     |
2026-01-26T14:33:47.5589708Z 159 |     with tempfile.TemporaryDirectory() as tmpdir:
2026-01-26T14:33:47.5589827Z 160 |         test_file = Path(tmpdir) / "cleanup_test.json"
2026-01-26T14:33:47.5589887Z 161 |         
2026-01-26T14:33:47.5589948Z     | ^^^^^^^^
2026-01-26T14:33:47.5590055Z 162 |         atomic_write(test_file, '{"test": true}')
2026-01-26T14:33:47.5590114Z     |
2026-01-26T14:33:47.5590197Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5590202Z 
2026-01-26T14:33:47.5590286Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5590368Z    --> test_transactional_save.py:163:1
2026-01-26T14:33:47.5590546Z     |
2026-01-26T14:33:47.5590647Z 162 |         atomic_write(test_file, '{"test": true}')
2026-01-26T14:33:47.5590712Z 163 |         
2026-01-26T14:33:47.5590771Z     | ^^^^^^^^
2026-01-26T14:33:47.5590980Z 164 |         temp_files = list(Path(tmpdir).glob(".*.tmp"))
2026-01-26T14:33:47.5591070Z 165 |         assert len(temp_files) == 0
2026-01-26T14:33:47.5591129Z     |
2026-01-26T14:33:47.5591213Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5591218Z 
2026-01-26T14:33:47.5591304Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5591389Z    --> test_transactional_save.py:166:1
2026-01-26T14:33:47.5591446Z     |
2026-01-26T14:33:47.5591557Z 164 |         temp_files = list(Path(tmpdir).glob(".*.tmp"))
2026-01-26T14:33:47.5591647Z 165 |         assert len(temp_files) == 0
2026-01-26T14:33:47.5591706Z 166 |         
2026-01-26T14:33:47.5591765Z     | ^^^^^^^^
2026-01-26T14:33:47.5591881Z 167 |         print("  [OK] No temporary files left behind")
2026-01-26T14:33:47.5591944Z     |
2026-01-26T14:33:47.5592037Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5592042Z 
2026-01-26T14:33:47.5592121Z E722 Do not use bare `except`
2026-01-26T14:33:47.5592215Z    --> test_transactional_save.py:175:9
2026-01-26T14:33:47.5592272Z     |
2026-01-26T14:33:47.5592333Z 173 |         try:
2026-01-26T14:33:47.5592433Z 174 |             INDEX_METADATA_FILE.unlink()
2026-01-26T14:33:47.5592498Z 175 |         except:
2026-01-26T14:33:47.5592561Z     |         ^^^^^^
2026-01-26T14:33:47.5592632Z 176 |             pass
2026-01-26T14:33:47.5592689Z     |
2026-01-26T14:33:47.5592694Z 
2026-01-26T14:33:47.5592777Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5592861Z    --> test_transactional_save.py:184:1
2026-01-26T14:33:47.5592924Z     |
2026-01-26T14:33:47.5592994Z 182 |     print("=" * 50)
2026-01-26T14:33:47.5593057Z 183 |     print()
2026-01-26T14:33:47.5593120Z 184 |     
2026-01-26T14:33:47.5593179Z     | ^^^^
2026-01-26T14:33:47.5593244Z 185 |     try:
2026-01-26T14:33:47.5593319Z 186 |         test_atomic_write()
2026-01-26T14:33:47.5593384Z     |
2026-01-26T14:33:47.5593470Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5593474Z 
2026-01-26T14:33:47.5593557Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5593644Z    --> test_transactional_save.py:192:1
2026-01-26T14:33:47.5593701Z     |
2026-01-26T14:33:47.5593781Z 190 |         test_concurrent_writes()
2026-01-26T14:33:47.5593858Z 191 |         test_metadata_save_load()
2026-01-26T14:33:47.5593923Z 192 |         
2026-01-26T14:33:47.5593983Z     | ^^^^^^^^
2026-01-26T14:33:47.5594046Z 193 |         print()
2026-01-26T14:33:47.5594120Z 194 |         print("=" * 50)
2026-01-26T14:33:47.5594181Z     |
2026-01-26T14:33:47.5594277Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5594282Z 
2026-01-26T14:33:47.5594393Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5594478Z  --> test_unicode_handling.py:2:1
2026-01-26T14:33:47.5594539Z   |
2026-01-26T14:33:47.5594648Z 1 |   """Tests for Unicode handling improvements"""
2026-01-26T14:33:47.5594719Z 2 | / import sys
2026-01-26T14:33:47.5594783Z 3 | | import os
2026-01-26T14:33:47.5594864Z 4 | | from pathlib import Path
2026-01-26T14:33:47.5594939Z 5 | | import tempfile
2026-01-26T14:33:47.5595002Z   | |_______________^
2026-01-26T14:33:47.5595059Z 6 |
2026-01-26T14:33:47.5595140Z 7 |   sys.path.append(os.getcwd())
2026-01-26T14:33:47.5595206Z   |
2026-01-26T14:33:47.5595277Z help: Organize imports
2026-01-26T14:33:47.5595282Z 
2026-01-26T14:33:47.5595362Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5595451Z   --> test_unicode_handling.py:15:1
2026-01-26T14:33:47.5595508Z    |
2026-01-26T14:33:47.5595595Z 13 |     """Test reading UTF-8 file"""
2026-01-26T14:33:47.5595677Z 14 |     print("Testing UTF-8 file...")
2026-01-26T14:33:47.5595742Z 15 |     
2026-01-26T14:33:47.5595802Z    | ^^^^
2026-01-26T14:33:47.5596076Z 16 |     with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False, suffix='.txt') as f:
2026-01-26T14:33:47.5596490Z 17 |         f.write("Hello Unicode: \u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430 \u043c\u043e\u0432\u0430 \U0001f600")
2026-01-26T14:33:47.5596550Z    |
2026-01-26T14:33:47.5596709Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5596715Z 
2026-01-26T14:33:47.5596802Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5596883Z   --> test_unicode_handling.py:19:1
2026-01-26T14:33:47.5596941Z    |
2026-01-26T14:33:47.5597248Z 17 |         f.write("Hello Unicode: \u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430 \u043c\u043e\u0432\u0430 \U0001f600")
2026-01-26T14:33:47.5597327Z 18 |         temp_path = Path(f.name)
2026-01-26T14:33:47.5597386Z 19 |     
2026-01-26T14:33:47.5597443Z    | ^^^^
2026-01-26T14:33:47.5597506Z 20 |     try:
2026-01-26T14:33:47.5597599Z 21 |         content = safe_read_text(temp_path)
2026-01-26T14:33:47.5597656Z    |
2026-01-26T14:33:47.5597750Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5597755Z 
2026-01-26T14:33:47.5597836Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5597917Z   --> test_unicode_handling.py:27:1
2026-01-26T14:33:47.5597974Z    |
2026-01-26T14:33:47.5598045Z 25 |     finally:
2026-01-26T14:33:47.5598123Z 26 |         temp_path.unlink()
2026-01-26T14:33:47.5598182Z 27 |     
2026-01-26T14:33:47.5598246Z    | ^^^^
2026-01-26T14:33:47.5598305Z 28 |
2026-01-26T14:33:47.5598382Z 29 | def test_latin1_file():
2026-01-26T14:33:47.5598440Z    |
2026-01-26T14:33:47.5598530Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5598536Z 
2026-01-26T14:33:47.5598616Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5598696Z   --> test_unicode_handling.py:32:1
2026-01-26T14:33:47.5598860Z    |
2026-01-26T14:33:47.5598948Z 30 |     """Test reading Latin-1 file"""
2026-01-26T14:33:47.5599036Z 31 |     print("Testing Latin-1 file...")
2026-01-26T14:33:47.5599102Z 32 |     
2026-01-26T14:33:47.5599163Z    | ^^^^
2026-01-26T14:33:47.5599385Z 33 |     with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.txt') as f:
2026-01-26T14:33:47.5599473Z 34 |         f.write(b"Caf\xe9 \xe0 la mode")
2026-01-26T14:33:47.5599537Z    |
2026-01-26T14:33:47.5599625Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5599630Z 
2026-01-26T14:33:47.5599711Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5599796Z   --> test_unicode_handling.py:36:1
2026-01-26T14:33:47.5599856Z    |
2026-01-26T14:33:47.5599940Z 34 |         f.write(b"Caf\xe9 \xe0 la mode")
2026-01-26T14:33:47.5600016Z 35 |         temp_path = Path(f.name)
2026-01-26T14:33:47.5600080Z 36 |     
2026-01-26T14:33:47.5600137Z    | ^^^^
2026-01-26T14:33:47.5600197Z 37 |     try:
2026-01-26T14:33:47.5600290Z 38 |         content = safe_read_text(temp_path)
2026-01-26T14:33:47.5600349Z    |
2026-01-26T14:33:47.5600433Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5600438Z 
2026-01-26T14:33:47.5600524Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5600608Z   --> test_unicode_handling.py:48:1
2026-01-26T14:33:47.5600664Z    |
2026-01-26T14:33:47.5600750Z 46 |     """Test reading Windows-1252 file"""
2026-01-26T14:33:47.5600852Z 47 |     print("Testing Windows-1252 file...")
2026-01-26T14:33:47.5600911Z 48 |     
2026-01-26T14:33:47.5600968Z    | ^^^^
2026-01-26T14:33:47.5601182Z 49 |     with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.txt') as f:
2026-01-26T14:33:47.5601286Z 50 |         f.write(b'Smart quotes: \x93text\x94')
2026-01-26T14:33:47.5601344Z    |
2026-01-26T14:33:47.5601428Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5601438Z 
2026-01-26T14:33:47.5601515Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5601593Z   --> test_unicode_handling.py:52:1
2026-01-26T14:33:47.5601649Z    |
2026-01-26T14:33:47.5601744Z 50 |         f.write(b'Smart quotes: \x93text\x94')
2026-01-26T14:33:47.5601818Z 51 |         temp_path = Path(f.name)
2026-01-26T14:33:47.5602008Z 52 |     
2026-01-26T14:33:47.5602072Z    | ^^^^
2026-01-26T14:33:47.5602132Z 53 |     try:
2026-01-26T14:33:47.5602225Z 54 |         content = safe_read_text(temp_path)
2026-01-26T14:33:47.5602283Z    |
2026-01-26T14:33:47.5602474Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5602480Z 
2026-01-26T14:33:47.5602564Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5602646Z   --> test_unicode_handling.py:64:1
2026-01-26T14:33:47.5602707Z    |
2026-01-26T14:33:47.5602799Z 62 |     """Test reading UTF-8 with BOM file"""
2026-01-26T14:33:47.5602886Z 63 |     print("Testing UTF-8 with BOM...")
2026-01-26T14:33:47.5602945Z 64 |     
2026-01-26T14:33:47.5603008Z    | ^^^^
2026-01-26T14:33:47.5603223Z 65 |     with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.txt') as f:
2026-01-26T14:33:47.5603325Z 66 |         f.write(b'\xef\xbb\xbfUTF-8 with BOM')
2026-01-26T14:33:47.5603388Z    |
2026-01-26T14:33:47.5603476Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5603485Z 
2026-01-26T14:33:47.5603568Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5603654Z   --> test_unicode_handling.py:68:1
2026-01-26T14:33:47.5603712Z    |
2026-01-26T14:33:47.5603804Z 66 |         f.write(b'\xef\xbb\xbfUTF-8 with BOM')
2026-01-26T14:33:47.5603889Z 67 |         temp_path = Path(f.name)
2026-01-26T14:33:47.5603954Z 68 |     
2026-01-26T14:33:47.5604014Z    | ^^^^
2026-01-26T14:33:47.5604073Z 69 |     try:
2026-01-26T14:33:47.5604169Z 70 |         content = safe_read_text(temp_path)
2026-01-26T14:33:47.5604229Z    |
2026-01-26T14:33:47.5604312Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5604317Z 
2026-01-26T14:33:47.5604397Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5604487Z   --> test_unicode_handling.py:80:1
2026-01-26T14:33:47.5604545Z    |
2026-01-26T14:33:47.5604684Z 78 |     """Test that nonexistent files raise appropriate error"""
2026-01-26T14:33:47.5604781Z 79 |     print("Testing nonexistent file...")
2026-01-26T14:33:47.5604849Z 80 |     
2026-01-26T14:33:47.5604908Z    | ^^^^
2026-01-26T14:33:47.5605033Z 81 |     temp_path = Path("nonexistent_test_file_12345.txt")
2026-01-26T14:33:47.5605092Z    |
2026-01-26T14:33:47.5605176Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5605184Z 
2026-01-26T14:33:47.5605264Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5605347Z   --> test_unicode_handling.py:82:1
2026-01-26T14:33:47.5605404Z    |
2026-01-26T14:33:47.5605523Z 81 |     temp_path = Path("nonexistent_test_file_12345.txt")
2026-01-26T14:33:47.5605587Z 82 |     
2026-01-26T14:33:47.5605645Z    | ^^^^
2026-01-26T14:33:47.5605704Z 83 |     try:
2026-01-26T14:33:47.5605792Z 84 |         content = safe_read_text(temp_path)
2026-01-26T14:33:47.5605854Z    |
2026-01-26T14:33:47.5605936Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5605941Z 
2026-01-26T14:33:47.5606075Z F841 Local variable `content` is assigned to but never used
2026-01-26T14:33:47.5606160Z   --> test_unicode_handling.py:84:9
2026-01-26T14:33:47.5606221Z    |
2026-01-26T14:33:47.5606280Z 83 |     try:
2026-01-26T14:33:47.5606376Z 84 |         content = safe_read_text(temp_path)
2026-01-26T14:33:47.5606440Z    |         ^^^^^^^
2026-01-26T14:33:47.5606589Z 85 |         print("  [FAIL] Nonexistent file should have raised error")
2026-01-26T14:33:47.5606660Z 86 |         sys.exit(1)
2026-01-26T14:33:47.5606724Z    |
2026-01-26T14:33:47.5606840Z help: Remove assignment to unused variable `content`
2026-01-26T14:33:47.5606845Z 
2026-01-26T14:33:47.5606941Z UP024 [*] Replace aliased errors with `OSError`
2026-01-26T14:33:47.5607032Z   --> test_unicode_handling.py:87:12
2026-01-26T14:33:47.5607089Z    |
2026-01-26T14:33:47.5607230Z 85 |         print("  [FAIL] Nonexistent file should have raised error")
2026-01-26T14:33:47.5607304Z 86 |         sys.exit(1)
2026-01-26T14:33:47.5607401Z 87 |     except (IOError, FileNotFoundError):
2026-01-26T14:33:47.5607476Z    |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5607599Z 88 |         print("  [OK] Nonexistent file properly rejected")
2026-01-26T14:33:47.5607748Z    |
2026-01-26T14:33:47.5607833Z help: Replace with builtin `OSError`
2026-01-26T14:33:47.5607838Z 
2026-01-26T14:33:47.5607921Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5608082Z   --> test_unicode_handling.py:96:1
2026-01-26T14:33:47.5608143Z    |
2026-01-26T14:33:47.5608211Z 94 |     print("=" * 50)
2026-01-26T14:33:47.5608289Z 95 |     print()
2026-01-26T14:33:47.5608358Z 96 |     
2026-01-26T14:33:47.5608417Z    | ^^^^
2026-01-26T14:33:47.5608475Z 97 |     try:
2026-01-26T14:33:47.5608551Z 98 |         test_utf8_file()
2026-01-26T14:33:47.5608608Z    |
2026-01-26T14:33:47.5608694Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5608699Z 
2026-01-26T14:33:47.5608886Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5608976Z    --> test_unicode_handling.py:103:1
2026-01-26T14:33:47.5609035Z     |
2026-01-26T14:33:47.5609114Z 101 |         test_windows1252_file()
2026-01-26T14:33:47.5609203Z 102 |         test_nonexistent_file()
2026-01-26T14:33:47.5609262Z 103 |         
2026-01-26T14:33:47.5609322Z     | ^^^^^^^^
2026-01-26T14:33:47.5609391Z 104 |         print()
2026-01-26T14:33:47.5609461Z 105 |         print("=" * 50)
2026-01-26T14:33:47.5609522Z     |
2026-01-26T14:33:47.5609609Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5609613Z 
2026-01-26T14:33:47.5609726Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5609812Z  --> tests/test_cache_manager.py:1:1
2026-01-26T14:33:47.5609870Z   |
2026-01-26T14:33:47.5609945Z 1 | / import unittest
2026-01-26T14:33:47.5610048Z 2 | | from unittest.mock import patch, MagicMock
2026-01-26T14:33:47.5610127Z 3 | | from pathlib import Path
2026-01-26T14:33:47.5610190Z 4 | | import time
2026-01-26T14:33:47.5610261Z 5 | | import sys
2026-01-26T14:33:47.5610323Z 6 | | import os
2026-01-26T14:33:47.5610383Z   | |_________^
2026-01-26T14:33:47.5610446Z 7 |
2026-01-26T14:33:47.5610657Z 8 |   sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
2026-01-26T14:33:47.5610718Z   |
2026-01-26T14:33:47.5610797Z help: Organize imports
2026-01-26T14:33:47.5610809Z 
2026-01-26T14:33:47.5610888Z F401 [*] `time` imported but unused
2026-01-26T14:33:47.5610975Z  --> tests/test_cache_manager.py:4:8
2026-01-26T14:33:47.5611033Z   |
2026-01-26T14:33:47.5611139Z 2 | from unittest.mock import patch, MagicMock
2026-01-26T14:33:47.5611219Z 3 | from pathlib import Path
2026-01-26T14:33:47.5611285Z 4 | import time
2026-01-26T14:33:47.5611354Z   |        ^^^^
2026-01-26T14:33:47.5611418Z 5 | import sys
2026-01-26T14:33:47.5611481Z 6 | import os
2026-01-26T14:33:47.5611539Z   |
2026-01-26T14:33:47.5611631Z help: Remove unused import: `time`
2026-01-26T14:33:47.5611637Z 
2026-01-26T14:33:47.5611741Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5616954Z   --> tests/test_cache_manager.py:10:1
2026-01-26T14:33:47.5617035Z    |
2026-01-26T14:33:47.5617280Z  8 | sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
2026-01-26T14:33:47.5617349Z  9 |
2026-01-26T14:33:47.5617493Z 10 | from cache_manager import LRUCache, TTLCache, FileCache
2026-01-26T14:33:47.5617586Z    | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5617649Z    |
2026-01-26T14:33:47.5617727Z help: Organize imports
2026-01-26T14:33:47.5617734Z 
2026-01-26T14:33:47.5617829Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5617922Z   --> tests/test_cache_manager.py:17:1
2026-01-26T14:33:47.5617982Z    |
2026-01-26T14:33:47.5618083Z 15 |         """Test basic get/put operations"""
2026-01-26T14:33:47.5618174Z 16 |         cache = LRUCache(capacity=3)
2026-01-26T14:33:47.5618236Z 17 |         
2026-01-26T14:33:47.5618296Z    | ^^^^^^^^
2026-01-26T14:33:47.5618382Z 18 |         cache.put("key1", "value1")
2026-01-26T14:33:47.5618463Z 19 |         cache.put("key2", "value2")
2026-01-26T14:33:47.5618521Z    |
2026-01-26T14:33:47.5618612Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5618935Z 
2026-01-26T14:33:47.5619040Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5619132Z   --> tests/test_cache_manager.py:20:1
2026-01-26T14:33:47.5619191Z    |
2026-01-26T14:33:47.5619278Z 18 |         cache.put("key1", "value1")
2026-01-26T14:33:47.5619524Z 19 |         cache.put("key2", "value2")
2026-01-26T14:33:47.5619590Z 20 |         
2026-01-26T14:33:47.5619650Z    | ^^^^^^^^
2026-01-26T14:33:47.5619787Z 21 |         self.assertEqual(cache.get("key1"), "value1")
2026-01-26T14:33:47.5619898Z 22 |         self.assertEqual(cache.get("key2"), "value2")
2026-01-26T14:33:47.5619957Z    |
2026-01-26T14:33:47.5620052Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5620058Z 
2026-01-26T14:33:47.5620142Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5620231Z   --> tests/test_cache_manager.py:23:1
2026-01-26T14:33:47.5620296Z    |
2026-01-26T14:33:47.5620408Z 21 |         self.assertEqual(cache.get("key1"), "value1")
2026-01-26T14:33:47.5620517Z 22 |         self.assertEqual(cache.get("key2"), "value2")
2026-01-26T14:33:47.5620578Z 23 |     
2026-01-26T14:33:47.5620643Z    | ^^^^
2026-01-26T14:33:47.5620732Z 24 |     def test_lru_cache_eviction(self):
2026-01-26T14:33:47.5620843Z 25 |         """Test that LRU eviction works correctly"""
2026-01-26T14:33:47.5620907Z    |
2026-01-26T14:33:47.5620996Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5621001Z 
2026-01-26T14:33:47.5621085Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5621179Z   --> tests/test_cache_manager.py:27:1
2026-01-26T14:33:47.5621238Z    |
2026-01-26T14:33:47.5621346Z 25 |         """Test that LRU eviction works correctly"""
2026-01-26T14:33:47.5621430Z 26 |         cache = LRUCache(capacity=2)
2026-01-26T14:33:47.5621498Z 27 |         
2026-01-26T14:33:47.5621558Z    | ^^^^^^^^
2026-01-26T14:33:47.5621638Z 28 |         cache.put("key1", "value1")
2026-01-26T14:33:47.5621723Z 29 |         cache.put("key2", "value2")
2026-01-26T14:33:47.5621784Z    |
2026-01-26T14:33:47.5621876Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5621881Z 
2026-01-26T14:33:47.5621962Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5622053Z   --> tests/test_cache_manager.py:31:1
2026-01-26T14:33:47.5622113Z    |
2026-01-26T14:33:47.5622196Z 29 |         cache.put("key2", "value2")
2026-01-26T14:33:47.5622282Z 30 |         cache.put("key3", "value3")
2026-01-26T14:33:47.5622343Z 31 |         
2026-01-26T14:33:47.5622404Z    | ^^^^^^^^
2026-01-26T14:33:47.5622509Z 32 |         self.assertIsNone(cache.get("key1"))
2026-01-26T14:33:47.5622627Z 33 |         self.assertEqual(cache.get("key2"), "value2")
2026-01-26T14:33:47.5622687Z    |
2026-01-26T14:33:47.5622774Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5622779Z 
2026-01-26T14:33:47.5622865Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5622951Z   --> tests/test_cache_manager.py:35:1
2026-01-26T14:33:47.5623009Z    |
2026-01-26T14:33:47.5623125Z 33 |         self.assertEqual(cache.get("key2"), "value2")
2026-01-26T14:33:47.5623235Z 34 |         self.assertEqual(cache.get("key3"), "value3")
2026-01-26T14:33:47.5623296Z 35 |     
2026-01-26T14:33:47.5623359Z    | ^^^^
2026-01-26T14:33:47.5623465Z 36 |     def test_lru_cache_update_existing(self):
2026-01-26T14:33:47.5623559Z 37 |         """Test updating existing key"""
2026-01-26T14:33:47.5623619Z    |
2026-01-26T14:33:47.5623712Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5623717Z 
2026-01-26T14:33:47.5623798Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5623882Z   --> tests/test_cache_manager.py:39:1
2026-01-26T14:33:47.5623949Z    |
2026-01-26T14:33:47.5624036Z 37 |         """Test updating existing key"""
2026-01-26T14:33:47.5624120Z 38 |         cache = LRUCache(capacity=2)
2026-01-26T14:33:47.5624180Z 39 |         
2026-01-26T14:33:47.5624243Z    | ^^^^^^^^
2026-01-26T14:33:47.5624323Z 40 |         cache.put("key1", "value1")
2026-01-26T14:33:47.5624401Z 41 |         cache.put("key2", "value2")
2026-01-26T14:33:47.5624579Z    |
2026-01-26T14:33:47.5624666Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5624671Z 
2026-01-26T14:33:47.5624750Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5624838Z   --> tests/test_cache_manager.py:43:1
2026-01-26T14:33:47.5624976Z    |
2026-01-26T14:33:47.5625056Z 41 |         cache.put("key2", "value2")
2026-01-26T14:33:47.5625140Z 42 |         cache.put("key1", "updated1")
2026-01-26T14:33:47.5625207Z 43 |         
2026-01-26T14:33:47.5625267Z    | ^^^^^^^^
2026-01-26T14:33:47.5625388Z 44 |         self.assertEqual(cache.get("key1"), "updated1")
2026-01-26T14:33:47.5625505Z 45 |         self.assertEqual(cache.get("key2"), "value2")
2026-01-26T14:33:47.5625564Z    |
2026-01-26T14:33:47.5625653Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5625657Z 
2026-01-26T14:33:47.5625746Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5625835Z   --> tests/test_cache_manager.py:46:1
2026-01-26T14:33:47.5625893Z    |
2026-01-26T14:33:47.5626012Z 44 |         self.assertEqual(cache.get("key1"), "updated1")
2026-01-26T14:33:47.5626125Z 45 |         self.assertEqual(cache.get("key2"), "value2")
2026-01-26T14:33:47.5626188Z 46 |     
2026-01-26T14:33:47.5626247Z    | ^^^^
2026-01-26T14:33:47.5626349Z 47 |     def test_lru_cache_access_order(self):
2026-01-26T14:33:47.5626467Z 48 |         """Test that accessing an item moves it to end"""
2026-01-26T14:33:47.5626525Z    |
2026-01-26T14:33:47.5626612Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5626617Z 
2026-01-26T14:33:47.5626704Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5626786Z   --> tests/test_cache_manager.py:50:1
2026-01-26T14:33:47.5626845Z    |
2026-01-26T14:33:47.5626962Z 48 |         """Test that accessing an item moves it to end"""
2026-01-26T14:33:47.5627047Z 49 |         cache = LRUCache(capacity=2)
2026-01-26T14:33:47.5627108Z 50 |         
2026-01-26T14:33:47.5627170Z    | ^^^^^^^^
2026-01-26T14:33:47.5627255Z 51 |         cache.put("key1", "value1")
2026-01-26T14:33:47.5627339Z 52 |         cache.put("key2", "value2")
2026-01-26T14:33:47.5627397Z    |
2026-01-26T14:33:47.5627487Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5627493Z 
2026-01-26T14:33:47.5627575Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5627657Z   --> tests/test_cache_manager.py:55:1
2026-01-26T14:33:47.5627720Z    |
2026-01-26T14:33:47.5627797Z 53 |         cache.get("key1")
2026-01-26T14:33:47.5627876Z 54 |         cache.put("key3", "value3")
2026-01-26T14:33:47.5627936Z 55 |         
2026-01-26T14:33:47.5628003Z    | ^^^^^^^^
2026-01-26T14:33:47.5628113Z 56 |         self.assertEqual(cache.get("key1"), "value1")
2026-01-26T14:33:47.5628210Z 57 |         self.assertIsNone(cache.get("key2"))
2026-01-26T14:33:47.5628273Z    |
2026-01-26T14:33:47.5628358Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5628363Z 
2026-01-26T14:33:47.5628444Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5628534Z   --> tests/test_cache_manager.py:58:1
2026-01-26T14:33:47.5628597Z    |
2026-01-26T14:33:47.5628705Z 56 |         self.assertEqual(cache.get("key1"), "value1")
2026-01-26T14:33:47.5628922Z 57 |         self.assertIsNone(cache.get("key2"))
2026-01-26T14:33:47.5628993Z 58 |     
2026-01-26T14:33:47.5629056Z    | ^^^^
2026-01-26T14:33:47.5629141Z 59 |     def test_lru_cache_stats(self):
2026-01-26T14:33:47.5629235Z 60 |         """Test cache statistics tracking"""
2026-01-26T14:33:47.5629295Z    |
2026-01-26T14:33:47.5629379Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5629384Z 
2026-01-26T14:33:47.5629465Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5629552Z   --> tests/test_cache_manager.py:62:1
2026-01-26T14:33:47.5629611Z    |
2026-01-26T14:33:47.5629700Z 60 |         """Test cache statistics tracking"""
2026-01-26T14:33:47.5629788Z 61 |         cache = LRUCache(capacity=2)
2026-01-26T14:33:47.5629848Z 62 |         
2026-01-26T14:33:47.5629907Z    | ^^^^^^^^
2026-01-26T14:33:47.5629985Z 63 |         cache.put("key1", "value1")
2026-01-26T14:33:47.5630305Z 64 |         cache.get("key1")
2026-01-26T14:33:47.5630365Z    |
2026-01-26T14:33:47.5630454Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5630459Z 
2026-01-26T14:33:47.5630644Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5630732Z   --> tests/test_cache_manager.py:66:1
2026-01-26T14:33:47.5630791Z    |
2026-01-26T14:33:47.5630867Z 64 |         cache.get("key1")
2026-01-26T14:33:47.5630937Z 65 |         cache.get("key2")
2026-01-26T14:33:47.5630997Z 66 |         
2026-01-26T14:33:47.5631056Z    | ^^^^^^^^
2026-01-26T14:33:47.5631140Z 67 |         stats = cache.get_stats()
2026-01-26T14:33:47.5631236Z 68 |         self.assertEqual(stats["hits"], 1)
2026-01-26T14:33:47.5631295Z    |
2026-01-26T14:33:47.5631388Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5631393Z 
2026-01-26T14:33:47.5631474Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5631555Z   --> tests/test_cache_manager.py:72:1
2026-01-26T14:33:47.5631617Z    |
2026-01-26T14:33:47.5631713Z 70 |         self.assertEqual(stats["size"], 1)
2026-01-26T14:33:47.5631814Z 71 |         self.assertEqual(stats["capacity"], 2)
2026-01-26T14:33:47.5631874Z 72 |     
2026-01-26T14:33:47.5631940Z    | ^^^^
2026-01-26T14:33:47.5632025Z 73 |     def test_lru_cache_clear(self):
2026-01-26T14:33:47.5632101Z 74 |         """Test clearing cache"""
2026-01-26T14:33:47.5632164Z    |
2026-01-26T14:33:47.5632249Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5632254Z 
2026-01-26T14:33:47.5632335Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5632417Z   --> tests/test_cache_manager.py:76:1
2026-01-26T14:33:47.5632479Z    |
2026-01-26T14:33:47.5632553Z 74 |         """Test clearing cache"""
2026-01-26T14:33:47.5632636Z 75 |         cache = LRUCache(capacity=2)
2026-01-26T14:33:47.5632703Z 76 |         
2026-01-26T14:33:47.5632764Z    | ^^^^^^^^
2026-01-26T14:33:47.5632844Z 77 |         cache.put("key1", "value1")
2026-01-26T14:33:47.5632928Z 78 |         cache.put("key2", "value2")
2026-01-26T14:33:47.5632992Z    |
2026-01-26T14:33:47.5633078Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5633083Z 
2026-01-26T14:33:47.5633163Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5633256Z   --> tests/test_cache_manager.py:80:1
2026-01-26T14:33:47.5633316Z    |
2026-01-26T14:33:47.5633393Z 78 |         cache.put("key2", "value2")
2026-01-26T14:33:47.5633472Z 79 |         cache.clear()
2026-01-26T14:33:47.5633531Z 80 |         
2026-01-26T14:33:47.5633590Z    | ^^^^^^^^
2026-01-26T14:33:47.5633684Z 81 |         self.assertIsNone(cache.get("key1"))
2026-01-26T14:33:47.5633810Z 82 |         self.assertEqual(cache.get_stats()["size"], 0)
2026-01-26T14:33:47.5633870Z    |
2026-01-26T14:33:47.5633955Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5633960Z 
2026-01-26T14:33:47.5634045Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5634127Z   --> tests/test_cache_manager.py:89:1
2026-01-26T14:33:47.5634190Z    |
2026-01-26T14:33:47.5634283Z 87 |         """Test basic get/put operations"""
2026-01-26T14:33:47.5634399Z 88 |         cache = TTLCache(ttl_seconds=10, max_size=3)
2026-01-26T14:33:47.5634459Z 89 |         
2026-01-26T14:33:47.5634518Z    | ^^^^^^^^
2026-01-26T14:33:47.5634604Z 90 |         cache.put("key1", "value1")
2026-01-26T14:33:47.5634680Z 91 |         cache.put("key2", "value2")
2026-01-26T14:33:47.5634739Z    |
2026-01-26T14:33:47.5634829Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5634833Z 
2026-01-26T14:33:47.5634913Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5634994Z   --> tests/test_cache_manager.py:92:1
2026-01-26T14:33:47.5635052Z    |
2026-01-26T14:33:47.5635132Z 90 |         cache.put("key1", "value1")
2026-01-26T14:33:47.5635209Z 91 |         cache.put("key2", "value2")
2026-01-26T14:33:47.5635268Z 92 |         
2026-01-26T14:33:47.5635332Z    | ^^^^^^^^
2026-01-26T14:33:47.5635442Z 93 |         self.assertEqual(cache.get("key1"), "value1")
2026-01-26T14:33:47.5635641Z 94 |         self.assertEqual(cache.get("key2"), "value2")
2026-01-26T14:33:47.5635710Z    |
2026-01-26T14:33:47.5635802Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5635807Z 
2026-01-26T14:33:47.5635960Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5636044Z   --> tests/test_cache_manager.py:95:1
2026-01-26T14:33:47.5636108Z    |
2026-01-26T14:33:47.5636215Z 93 |         self.assertEqual(cache.get("key1"), "value1")
2026-01-26T14:33:47.5636324Z 94 |         self.assertEqual(cache.get("key2"), "value2")
2026-01-26T14:33:47.5636390Z 95 |     
2026-01-26T14:33:47.5636449Z    | ^^^^
2026-01-26T14:33:47.5636526Z 96 |     @patch('time.time')
2026-01-26T14:33:47.5636645Z 97 |     def test_ttl_cache_expiration(self, mock_time):
2026-01-26T14:33:47.5636709Z    |
2026-01-26T14:33:47.5636793Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5636798Z 
2026-01-26T14:33:47.5636879Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5636971Z    --> tests/test_cache_manager.py:100:1
2026-01-26T14:33:47.5637035Z     |
2026-01-26T14:33:47.5637136Z  98 |         """Test that items expire after TTL"""
2026-01-26T14:33:47.5637248Z  99 |         cache = TTLCache(ttl_seconds=5, max_size=10)
2026-01-26T14:33:47.5637312Z 100 |         
2026-01-26T14:33:47.5637372Z     | ^^^^^^^^
2026-01-26T14:33:47.5637463Z 101 |         mock_time.return_value = 100.0
2026-01-26T14:33:47.5637550Z 102 |         cache.put("key1", "value1")
2026-01-26T14:33:47.5637608Z     |
2026-01-26T14:33:47.5637694Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5637699Z 
2026-01-26T14:33:47.5637786Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5637874Z    --> tests/test_cache_manager.py:103:1
2026-01-26T14:33:47.5637935Z     |
2026-01-26T14:33:47.5638022Z 101 |         mock_time.return_value = 100.0
2026-01-26T14:33:47.5638106Z 102 |         cache.put("key1", "value1")
2026-01-26T14:33:47.5638167Z 103 |         
2026-01-26T14:33:47.5638227Z     | ^^^^^^^^
2026-01-26T14:33:47.5638323Z 104 |         mock_time.return_value = 104.0
2026-01-26T14:33:47.5638444Z 105 |         self.assertEqual(cache.get("key1"), "value1")
2026-01-26T14:33:47.5638508Z     |
2026-01-26T14:33:47.5638600Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5638608Z 
2026-01-26T14:33:47.5638690Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5638875Z    --> tests/test_cache_manager.py:106:1
2026-01-26T14:33:47.5638937Z     |
2026-01-26T14:33:47.5639032Z 104 |         mock_time.return_value = 104.0
2026-01-26T14:33:47.5639148Z 105 |         self.assertEqual(cache.get("key1"), "value1")
2026-01-26T14:33:47.5639213Z 106 |         
2026-01-26T14:33:47.5639279Z     | ^^^^^^^^
2026-01-26T14:33:47.5639364Z 107 |         mock_time.return_value = 106.0
2026-01-26T14:33:47.5639462Z 108 |         self.assertIsNone(cache.get("key1"))
2026-01-26T14:33:47.5639522Z     |
2026-01-26T14:33:47.5639613Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5639618Z 
2026-01-26T14:33:47.5639706Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5639791Z    --> tests/test_cache_manager.py:109:1
2026-01-26T14:33:47.5639860Z     |
2026-01-26T14:33:47.5639943Z 107 |         mock_time.return_value = 106.0
2026-01-26T14:33:47.5640041Z 108 |         self.assertIsNone(cache.get("key1"))
2026-01-26T14:33:47.5640109Z 109 |     
2026-01-26T14:33:47.5640170Z     | ^^^^
2026-01-26T14:33:47.5640278Z 110 |     def test_ttl_cache_max_size_eviction(self):
2026-01-26T14:33:47.5640386Z 111 |         """Test eviction when max size is reached"""
2026-01-26T14:33:47.5640450Z     |
2026-01-26T14:33:47.5640535Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5640540Z 
2026-01-26T14:33:47.5640624Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5640713Z    --> tests/test_cache_manager.py:113:1
2026-01-26T14:33:47.5640771Z     |
2026-01-26T14:33:47.5640874Z 111 |         """Test eviction when max size is reached"""
2026-01-26T14:33:47.5640985Z 112 |         cache = TTLCache(ttl_seconds=60, max_size=2)
2026-01-26T14:33:47.5641168Z 113 |         
2026-01-26T14:33:47.5641229Z     | ^^^^^^^^
2026-01-26T14:33:47.5641314Z 114 |         cache.put("key1", "value1")
2026-01-26T14:33:47.5641401Z 115 |         cache.put("key2", "value2")
2026-01-26T14:33:47.5641558Z     |
2026-01-26T14:33:47.5641647Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5641653Z 
2026-01-26T14:33:47.5641741Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5641827Z    --> tests/test_cache_manager.py:117:1
2026-01-26T14:33:47.5641886Z     |
2026-01-26T14:33:47.5641967Z 115 |         cache.put("key2", "value2")
2026-01-26T14:33:47.5642051Z 116 |         cache.put("key3", "value3")
2026-01-26T14:33:47.5642113Z 117 |         
2026-01-26T14:33:47.5642172Z     | ^^^^^^^^
2026-01-26T14:33:47.5642256Z 118 |         stats = cache.get_stats()
2026-01-26T14:33:47.5642353Z 119 |         self.assertEqual(stats["size"], 2)
2026-01-26T14:33:47.5642414Z     |
2026-01-26T14:33:47.5642505Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5642514Z 
2026-01-26T14:33:47.5642595Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5642677Z    --> tests/test_cache_manager.py:120:1
2026-01-26T14:33:47.5642736Z     |
2026-01-26T14:33:47.5642822Z 118 |         stats = cache.get_stats()
2026-01-26T14:33:47.5642917Z 119 |         self.assertEqual(stats["size"], 2)
2026-01-26T14:33:47.5642976Z 120 |     
2026-01-26T14:33:47.5643040Z     | ^^^^
2026-01-26T14:33:47.5643118Z 121 |     @patch('time.time')
2026-01-26T14:33:47.5643248Z 122 |     def test_ttl_cache_cleanup_expired(self, mock_time):
2026-01-26T14:33:47.5643308Z     |
2026-01-26T14:33:47.5643398Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5643402Z 
2026-01-26T14:33:47.5643483Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5643565Z    --> tests/test_cache_manager.py:125:1
2026-01-26T14:33:47.5643629Z     |
2026-01-26T14:33:47.5643737Z 123 |         """Test manual cleanup of expired items"""
2026-01-26T14:33:47.5643845Z 124 |         cache = TTLCache(ttl_seconds=5, max_size=10)
2026-01-26T14:33:47.5643914Z 125 |         
2026-01-26T14:33:47.5643974Z     | ^^^^^^^^
2026-01-26T14:33:47.5644062Z 126 |         mock_time.return_value = 100.0
2026-01-26T14:33:47.5644143Z 127 |         cache.put("key1", "value1")
2026-01-26T14:33:47.5644208Z     |
2026-01-26T14:33:47.5644292Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5644298Z 
2026-01-26T14:33:47.5644378Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5644467Z    --> tests/test_cache_manager.py:129:1
2026-01-26T14:33:47.5644526Z     |
2026-01-26T14:33:47.5644606Z 127 |         cache.put("key1", "value1")
2026-01-26T14:33:47.5644692Z 128 |         cache.put("key2", "value2")
2026-01-26T14:33:47.5644754Z 129 |         
2026-01-26T14:33:47.5644814Z     | ^^^^^^^^
2026-01-26T14:33:47.5644899Z 130 |         mock_time.return_value = 110.0
2026-01-26T14:33:47.5644999Z 131 |         removed = cache.cleanup_expired()
2026-01-26T14:33:47.5645057Z     |
2026-01-26T14:33:47.5645146Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5645151Z 
2026-01-26T14:33:47.5645245Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5645331Z    --> tests/test_cache_manager.py:132:1
2026-01-26T14:33:47.5645390Z     |
2026-01-26T14:33:47.5645479Z 130 |         mock_time.return_value = 110.0
2026-01-26T14:33:47.5645576Z 131 |         removed = cache.cleanup_expired()
2026-01-26T14:33:47.5645637Z 132 |         
2026-01-26T14:33:47.5645697Z     | ^^^^^^^^
2026-01-26T14:33:47.5645790Z 133 |         self.assertEqual(removed, 2)
2026-01-26T14:33:47.5645910Z 134 |         self.assertEqual(cache.get_stats()["size"], 0)
2026-01-26T14:33:47.5645970Z     |
2026-01-26T14:33:47.5646058Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5646068Z 
2026-01-26T14:33:47.5646147Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5646230Z    --> tests/test_cache_manager.py:135:1
2026-01-26T14:33:47.5646290Z     |
2026-01-26T14:33:47.5646382Z 133 |         self.assertEqual(removed, 2)
2026-01-26T14:33:47.5646588Z 134 |         self.assertEqual(cache.get_stats()["size"], 0)
2026-01-26T14:33:47.5646649Z 135 |     
2026-01-26T14:33:47.5646714Z     | ^^^^
2026-01-26T14:33:47.5646799Z 136 |     def test_ttl_cache_stats(self):
2026-01-26T14:33:47.5646969Z 137 |         """Test cache statistics tracking"""
2026-01-26T14:33:47.5647031Z     |
2026-01-26T14:33:47.5647125Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5647131Z 
2026-01-26T14:33:47.5647219Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5647304Z    --> tests/test_cache_manager.py:139:1
2026-01-26T14:33:47.5647369Z     |
2026-01-26T14:33:47.5647461Z 137 |         """Test cache statistics tracking"""
2026-01-26T14:33:47.5647570Z 138 |         cache = TTLCache(ttl_seconds=60, max_size=10)
2026-01-26T14:33:47.5647634Z 139 |         
2026-01-26T14:33:47.5647694Z     | ^^^^^^^^
2026-01-26T14:33:47.5647774Z 140 |         cache.put("key1", "value1")
2026-01-26T14:33:47.5647853Z 141 |         cache.get("key1")
2026-01-26T14:33:47.5647922Z     |
2026-01-26T14:33:47.5648007Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5648012Z 
2026-01-26T14:33:47.5648093Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5648185Z    --> tests/test_cache_manager.py:143:1
2026-01-26T14:33:47.5648244Z     |
2026-01-26T14:33:47.5648313Z 141 |         cache.get("key1")
2026-01-26T14:33:47.5648384Z 142 |         cache.get("key2")
2026-01-26T14:33:47.5648452Z 143 |         
2026-01-26T14:33:47.5648513Z     | ^^^^^^^^
2026-01-26T14:33:47.5648591Z 144 |         stats = cache.get_stats()
2026-01-26T14:33:47.5648690Z 145 |         self.assertEqual(stats["hits"], 1)
2026-01-26T14:33:47.5648751Z     |
2026-01-26T14:33:47.5649132Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5649143Z 
2026-01-26T14:33:47.5649282Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5649412Z    --> tests/test_cache_manager.py:149:1
2026-01-26T14:33:47.5649504Z     |
2026-01-26T14:33:47.5649656Z 147 |         self.assertEqual(stats["size"], 1)
2026-01-26T14:33:47.5649859Z 148 |         self.assertEqual(stats["ttl_seconds"], 60)
2026-01-26T14:33:47.5649970Z 149 |     
2026-01-26T14:33:47.5650033Z     | ^^^^
2026-01-26T14:33:47.5650124Z 150 |     def test_ttl_cache_clear(self):
2026-01-26T14:33:47.5650207Z 151 |         """Test clearing cache"""
2026-01-26T14:33:47.5650273Z     |
2026-01-26T14:33:47.5650362Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5650368Z 
2026-01-26T14:33:47.5650450Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5650535Z    --> tests/test_cache_manager.py:153:1
2026-01-26T14:33:47.5650601Z     |
2026-01-26T14:33:47.5650683Z 151 |         """Test clearing cache"""
2026-01-26T14:33:47.5650794Z 152 |         cache = TTLCache(ttl_seconds=60, max_size=10)
2026-01-26T14:33:47.5650861Z 153 |         
2026-01-26T14:33:47.5650921Z     | ^^^^^^^^
2026-01-26T14:33:47.5651005Z 154 |         cache.put("key1", "value1")
2026-01-26T14:33:47.5651084Z 155 |         cache.put("key2", "value2")
2026-01-26T14:33:47.5651151Z     |
2026-01-26T14:33:47.5651236Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5651241Z 
2026-01-26T14:33:47.5651335Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5651430Z    --> tests/test_cache_manager.py:157:1
2026-01-26T14:33:47.5651490Z     |
2026-01-26T14:33:47.5651570Z 155 |         cache.put("key2", "value2")
2026-01-26T14:33:47.5651652Z 156 |         cache.clear()
2026-01-26T14:33:47.5651717Z 157 |         
2026-01-26T14:33:47.5651777Z     | ^^^^^^^^
2026-01-26T14:33:47.5651878Z 158 |         self.assertIsNone(cache.get("key1"))
2026-01-26T14:33:47.5652004Z 159 |         self.assertEqual(cache.get_stats()["size"], 0)
2026-01-26T14:33:47.5652070Z     |
2026-01-26T14:33:47.5652164Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5652168Z 
2026-01-26T14:33:47.5652256Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5652347Z    --> tests/test_cache_manager.py:167:1
2026-01-26T14:33:47.5652429Z     |
2026-01-26T14:33:47.5652689Z 165 |         """Test basic file cache operations"""
2026-01-26T14:33:47.5652797Z 166 |         cache = FileCache(capacity=3)
2026-01-26T14:33:47.5652857Z 167 |         
2026-01-26T14:33:47.5652917Z     | ^^^^^^^^
2026-01-26T14:33:47.5653145Z 168 |         mock_stat_result = MagicMock()
2026-01-26T14:33:47.5653245Z 169 |         mock_stat_result.st_mtime = 123.45
2026-01-26T14:33:47.5653304Z     |
2026-01-26T14:33:47.5653389Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5653399Z 
2026-01-26T14:33:47.5653480Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5653564Z    --> tests/test_cache_manager.py:171:1
2026-01-26T14:33:47.5653622Z     |
2026-01-26T14:33:47.5653717Z 169 |         mock_stat_result.st_mtime = 123.45
2026-01-26T14:33:47.5653823Z 170 |         mock_stat.return_value = mock_stat_result
2026-01-26T14:33:47.5653883Z 171 |         
2026-01-26T14:33:47.5653948Z     | ^^^^^^^^
2026-01-26T14:33:47.5654035Z 172 |         file_path = Path("test.txt")
2026-01-26T14:33:47.5654134Z 173 |         cache.put(file_path, "file content")
2026-01-26T14:33:47.5654192Z     |
2026-01-26T14:33:47.5654282Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5654287Z 
2026-01-26T14:33:47.5654384Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5654471Z    --> tests/test_cache_manager.py:174:1
2026-01-26T14:33:47.5654535Z     |
2026-01-26T14:33:47.5654626Z 172 |         file_path = Path("test.txt")
2026-01-26T14:33:47.5654717Z 173 |         cache.put(file_path, "file content")
2026-01-26T14:33:47.5654784Z 174 |         
2026-01-26T14:33:47.5654844Z     | ^^^^^^^^
2026-01-26T14:33:47.5654927Z 175 |         result = cache.get(file_path)
2026-01-26T14:33:47.5655044Z 176 |         self.assertEqual(result, "file content")
2026-01-26T14:33:47.5655122Z     |
2026-01-26T14:33:47.5655206Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5655211Z 
2026-01-26T14:33:47.5655291Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5655380Z    --> tests/test_cache_manager.py:177:1
2026-01-26T14:33:47.5655445Z     |
2026-01-26T14:33:47.5655527Z 175 |         result = cache.get(file_path)
2026-01-26T14:33:47.5655636Z 176 |         self.assertEqual(result, "file content")
2026-01-26T14:33:47.5655701Z 177 |     
2026-01-26T14:33:47.5655764Z     | ^^^^
2026-01-26T14:33:47.5655855Z 178 |     @patch('pathlib.Path.stat')
2026-01-26T14:33:47.5656034Z 179 |     def test_file_cache_invalidation_on_mtime_change(self, mock_stat):
2026-01-26T14:33:47.5656094Z     |
2026-01-26T14:33:47.5656183Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5656188Z 
2026-01-26T14:33:47.5656274Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5656359Z    --> tests/test_cache_manager.py:182:1
2026-01-26T14:33:47.5656418Z     |
2026-01-26T14:33:47.5656564Z 180 |         """Test that cache is invalidated when file is modified"""
2026-01-26T14:33:47.5656653Z 181 |         cache = FileCache(capacity=3)
2026-01-26T14:33:47.5656714Z 182 |         
2026-01-26T14:33:47.5656778Z     | ^^^^^^^^
2026-01-26T14:33:47.5656873Z 183 |         mock_stat_result = MagicMock()
2026-01-26T14:33:47.5656963Z 184 |         mock_stat_result.st_mtime = 123.45
2026-01-26T14:33:47.5657022Z     |
2026-01-26T14:33:47.5657108Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5657122Z 
2026-01-26T14:33:47.5657202Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5657288Z    --> tests/test_cache_manager.py:186:1
2026-01-26T14:33:47.5657347Z     |
2026-01-26T14:33:47.5657441Z 184 |         mock_stat_result.st_mtime = 123.45
2026-01-26T14:33:47.5657550Z 185 |         mock_stat.return_value = mock_stat_result
2026-01-26T14:33:47.5657610Z 186 |         
2026-01-26T14:33:47.5657674Z     | ^^^^^^^^
2026-01-26T14:33:47.5657756Z 187 |         file_path = Path("test.txt")
2026-01-26T14:33:47.5657853Z 188 |         cache.put(file_path, "old content")
2026-01-26T14:33:47.5657913Z     |
2026-01-26T14:33:47.5658002Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5658007Z 
2026-01-26T14:33:47.5658182Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5658265Z    --> tests/test_cache_manager.py:189:1
2026-01-26T14:33:47.5658334Z     |
2026-01-26T14:33:47.5658416Z 187 |         file_path = Path("test.txt")
2026-01-26T14:33:47.5658583Z 188 |         cache.put(file_path, "old content")
2026-01-26T14:33:47.5658651Z 189 |         
2026-01-26T14:33:47.5658711Z     | ^^^^^^^^
2026-01-26T14:33:47.5658981Z 190 |         self.assertEqual(cache.get(file_path), "old content")
2026-01-26T14:33:47.5659045Z     |
2026-01-26T14:33:47.5659139Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5659144Z 
2026-01-26T14:33:47.5659225Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5659309Z    --> tests/test_cache_manager.py:191:1
2026-01-26T14:33:47.5659374Z     |
2026-01-26T14:33:47.5659513Z 190 |         self.assertEqual(cache.get(file_path), "old content")
2026-01-26T14:33:47.5659576Z 191 |         
2026-01-26T14:33:47.5659635Z     | ^^^^^^^^
2026-01-26T14:33:47.5659734Z 192 |         mock_stat_result.st_mtime = 124.45
2026-01-26T14:33:47.5659846Z 193 |         self.assertIsNone(cache.get(file_path))
2026-01-26T14:33:47.5659907Z     |
2026-01-26T14:33:47.5659999Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5660004Z 
2026-01-26T14:33:47.5660089Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5660174Z    --> tests/test_cache_manager.py:194:1
2026-01-26T14:33:47.5660241Z     |
2026-01-26T14:33:47.5660334Z 192 |         mock_stat_result.st_mtime = 124.45
2026-01-26T14:33:47.5660438Z 193 |         self.assertIsNone(cache.get(file_path))
2026-01-26T14:33:47.5660499Z 194 |     
2026-01-26T14:33:47.5660563Z     | ^^^^
2026-01-26T14:33:47.5660651Z 195 |     @patch('pathlib.Path.stat')
2026-01-26T14:33:47.5660790Z 196 |     def test_file_cache_miss_on_stat_error(self, mock_stat):
2026-01-26T14:33:47.5660856Z     |
2026-01-26T14:33:47.5660942Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5660948Z 
2026-01-26T14:33:47.5661028Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5661122Z    --> tests/test_cache_manager.py:199:1
2026-01-26T14:33:47.5661182Z     |
2026-01-26T14:33:47.5661302Z 197 |         """Test that cache returns None on stat errors"""
2026-01-26T14:33:47.5661390Z 198 |         cache = FileCache(capacity=3)
2026-01-26T14:33:47.5661457Z 199 |         
2026-01-26T14:33:47.5661517Z     | ^^^^^^^^
2026-01-26T14:33:47.5661637Z 200 |         mock_stat.side_effect = FileNotFoundError()
2026-01-26T14:33:47.5661702Z     |
2026-01-26T14:33:47.5661787Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5661792Z 
2026-01-26T14:33:47.5661872Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5661961Z    --> tests/test_cache_manager.py:201:1
2026-01-26T14:33:47.5662020Z     |
2026-01-26T14:33:47.5662131Z 200 |         mock_stat.side_effect = FileNotFoundError()
2026-01-26T14:33:47.5662191Z 201 |         
2026-01-26T14:33:47.5662256Z     | ^^^^^^^^
2026-01-26T14:33:47.5662352Z 202 |         file_path = Path("nonexistent.txt")
2026-01-26T14:33:47.5662442Z 203 |         result = cache.get(file_path)
2026-01-26T14:33:47.5662509Z     |
2026-01-26T14:33:47.5662599Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5662604Z 
2026-01-26T14:33:47.5662689Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5662778Z    --> tests/test_cache_manager.py:204:1
2026-01-26T14:33:47.5662842Z     |
2026-01-26T14:33:47.5662937Z 202 |         file_path = Path("nonexistent.txt")
2026-01-26T14:33:47.5663020Z 203 |         result = cache.get(file_path)
2026-01-26T14:33:47.5663085Z 204 |         
2026-01-26T14:33:47.5663146Z     | ^^^^^^^^
2026-01-26T14:33:47.5663228Z 205 |         self.assertIsNone(result)
2026-01-26T14:33:47.5663288Z     |
2026-01-26T14:33:47.5663379Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5663383Z 
2026-01-26T14:33:47.5663468Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5663549Z    --> tests/test_cache_manager.py:206:1
2026-01-26T14:33:47.5663614Z     |
2026-01-26T14:33:47.5663874Z 205 |         self.assertIsNone(result)
2026-01-26T14:33:47.5663937Z 206 |     
2026-01-26T14:33:47.5664002Z     | ^^^^
2026-01-26T14:33:47.5664086Z 207 |     @patch('pathlib.Path.stat')
2026-01-26T14:33:47.5664190Z 208 |     def test_file_cache_stats(self, mock_stat):
2026-01-26T14:33:47.5664347Z     |
2026-01-26T14:33:47.5664441Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5664446Z 
2026-01-26T14:33:47.5664526Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5664613Z    --> tests/test_cache_manager.py:211:1
2026-01-26T14:33:47.5664677Z     |
2026-01-26T14:33:47.5664765Z 209 |         """Test file cache statistics"""
2026-01-26T14:33:47.5664848Z 210 |         cache = FileCache(capacity=3)
2026-01-26T14:33:47.5664914Z 211 |         
2026-01-26T14:33:47.5664974Z     | ^^^^^^^^
2026-01-26T14:33:47.5665062Z 212 |         mock_stat_result = MagicMock()
2026-01-26T14:33:47.5665151Z 213 |         mock_stat_result.st_mtime = 123.45
2026-01-26T14:33:47.5665215Z     |
2026-01-26T14:33:47.5665302Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5665307Z 
2026-01-26T14:33:47.5665388Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5665478Z    --> tests/test_cache_manager.py:215:1
2026-01-26T14:33:47.5665539Z     |
2026-01-26T14:33:47.5665630Z 213 |         mock_stat_result.st_mtime = 123.45
2026-01-26T14:33:47.5665735Z 214 |         mock_stat.return_value = mock_stat_result
2026-01-26T14:33:47.5665800Z 215 |         
2026-01-26T14:33:47.5665859Z     | ^^^^^^^^
2026-01-26T14:33:47.5665941Z 216 |         file_path = Path("test.txt")
2026-01-26T14:33:47.5666037Z 217 |         cache.put(file_path, "content")
2026-01-26T14:33:47.5666096Z     |
2026-01-26T14:33:47.5666180Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5666185Z 
2026-01-26T14:33:47.5666270Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5666352Z    --> tests/test_cache_manager.py:218:1
2026-01-26T14:33:47.5666410Z     |
2026-01-26T14:33:47.5666492Z 216 |         file_path = Path("test.txt")
2026-01-26T14:33:47.5666591Z 217 |         cache.put(file_path, "content")
2026-01-26T14:33:47.5666652Z 218 |         
2026-01-26T14:33:47.5666711Z     | ^^^^^^^^
2026-01-26T14:33:47.5666801Z 219 |         result1 = cache.get(file_path)
2026-01-26T14:33:47.5666902Z 220 |         self.assertEqual(result1, "content")
2026-01-26T14:33:47.5666962Z     |
2026-01-26T14:33:47.5667048Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5667058Z 
2026-01-26T14:33:47.5667138Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5667220Z    --> tests/test_cache_manager.py:221:1
2026-01-26T14:33:47.5667280Z     |
2026-01-26T14:33:47.5667369Z 219 |         result1 = cache.get(file_path)
2026-01-26T14:33:47.5667464Z 220 |         self.assertEqual(result1, "content")
2026-01-26T14:33:47.5667525Z 221 |         
2026-01-26T14:33:47.5667592Z     | ^^^^^^^^
2026-01-26T14:33:47.5667670Z 222 |         stats = cache.get_stats()
2026-01-26T14:33:47.5667764Z 223 |         self.assertEqual(stats["hits"], 1)
2026-01-26T14:33:47.5667826Z     |
2026-01-26T14:33:47.5667916Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5667921Z 
2026-01-26T14:33:47.5668043Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5668127Z    --> tests/test_cache_manager.py:225:1
2026-01-26T14:33:47.5668194Z     |
2026-01-26T14:33:47.5668284Z 223 |         self.assertEqual(stats["hits"], 1)
2026-01-26T14:33:47.5668386Z 224 |         self.assertEqual(stats["capacity"], 3)
2026-01-26T14:33:47.5668445Z 225 |     
2026-01-26T14:33:47.5668510Z     | ^^^^
2026-01-26T14:33:47.5668594Z 226 |     @patch('pathlib.Path.stat')
2026-01-26T14:33:47.5668696Z 227 |     def test_file_cache_clear(self, mock_stat):
2026-01-26T14:33:47.5668857Z     |
2026-01-26T14:33:47.5668944Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5668949Z 
2026-01-26T14:33:47.5669030Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5669119Z    --> tests/test_cache_manager.py:230:1
2026-01-26T14:33:47.5669178Z     |
2026-01-26T14:33:47.5669392Z 228 |         """Test clearing file cache"""
2026-01-26T14:33:47.5669477Z 229 |         cache = FileCache(capacity=3)
2026-01-26T14:33:47.5669545Z 230 |         
2026-01-26T14:33:47.5669604Z     | ^^^^^^^^
2026-01-26T14:33:47.5669790Z 231 |         mock_stat_result = MagicMock()
2026-01-26T14:33:47.5669886Z 232 |         mock_stat_result.st_mtime = 123.45
2026-01-26T14:33:47.5669945Z     |
2026-01-26T14:33:47.5670032Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5670037Z 
2026-01-26T14:33:47.5670122Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5670205Z    --> tests/test_cache_manager.py:234:1
2026-01-26T14:33:47.5670264Z     |
2026-01-26T14:33:47.5670356Z 232 |         mock_stat_result.st_mtime = 123.45
2026-01-26T14:33:47.5670463Z 233 |         mock_stat.return_value = mock_stat_result
2026-01-26T14:33:47.5670523Z 234 |         
2026-01-26T14:33:47.5670583Z     | ^^^^^^^^
2026-01-26T14:33:47.5670668Z 235 |         file_path = Path("test.txt")
2026-01-26T14:33:47.5670758Z 236 |         cache.put(file_path, "content")
2026-01-26T14:33:47.5670818Z     |
2026-01-26T14:33:47.5670903Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5670907Z 
2026-01-26T14:33:47.5670992Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5671078Z    --> tests/test_cache_manager.py:238:1
2026-01-26T14:33:47.5671137Z     |
2026-01-26T14:33:47.5671232Z 236 |         cache.put(file_path, "content")
2026-01-26T14:33:47.5671305Z 237 |         cache.clear()
2026-01-26T14:33:47.5671366Z 238 |         
2026-01-26T14:33:47.5671431Z     | ^^^^^^^^
2026-01-26T14:33:47.5671534Z 239 |         self.assertIsNone(cache.get(file_path))
2026-01-26T14:33:47.5671593Z     |
2026-01-26T14:33:47.5671681Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5671685Z 
2026-01-26T14:33:47.5671796Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5671878Z  --> tests/test_config.py:1:1
2026-01-26T14:33:47.5671937Z   |
2026-01-26T14:33:47.5672012Z 1 | / import unittest
2026-01-26T14:33:47.5672115Z 2 | | from unittest.mock import patch, MagicMock
2026-01-26T14:33:47.5672196Z 3 | | from pathlib import Path
2026-01-26T14:33:47.5672262Z 4 | | import sys
2026-01-26T14:33:47.5672331Z 5 | | import os
2026-01-26T14:33:47.5672393Z   | |_________^
2026-01-26T14:33:47.5672458Z 6 |
2026-01-26T14:33:47.5672670Z 7 |   sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
2026-01-26T14:33:47.5672731Z   |
2026-01-26T14:33:47.5672804Z help: Organize imports
2026-01-26T14:33:47.5672809Z 
2026-01-26T14:33:47.5672934Z F401 [*] `unittest.mock.MagicMock` imported but unused
2026-01-26T14:33:47.5673016Z  --> tests/test_config.py:2:34
2026-01-26T14:33:47.5673075Z   |
2026-01-26T14:33:47.5673142Z 1 | import unittest
2026-01-26T14:33:47.5673247Z 2 | from unittest.mock import patch, MagicMock
2026-01-26T14:33:47.5673322Z   |                                  ^^^^^^^^^
2026-01-26T14:33:47.5673400Z 3 | from pathlib import Path
2026-01-26T14:33:47.5673468Z 4 | import sys
2026-01-26T14:33:47.5673532Z   |
2026-01-26T14:33:47.5673653Z help: Remove unused import: `unittest.mock.MagicMock`
2026-01-26T14:33:47.5673658Z 
2026-01-26T14:33:47.5673760Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5673846Z   --> tests/test_config.py:9:1
2026-01-26T14:33:47.5673909Z    |
2026-01-26T14:33:47.5674109Z  7 |   sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
2026-01-26T14:33:47.5674173Z  8 |
2026-01-26T14:33:47.5674247Z  9 | / from config import (
2026-01-26T14:33:47.5674318Z 10 | |     validate_path,
2026-01-26T14:33:47.5674405Z 11 | |     safe_read_text,
2026-01-26T14:33:47.5674485Z 12 | |     get_max_file_size_bytes,
2026-01-26T14:33:47.5674563Z 13 | |     get_max_memory_bytes,
2026-01-26T14:33:47.5674635Z 14 | |     get_ignored_dirs,
2026-01-26T14:33:47.5674711Z 15 | |     PROJECT_ROOT,
2026-01-26T14:33:47.5674780Z 16 | |     MAX_FILE_SIZE_MB,
2026-01-26T14:33:47.5674849Z 17 | |     MAX_MEMORY_MB,
2026-01-26T14:33:47.5674913Z 18 | | )
2026-01-26T14:33:47.5675061Z    | |_^
2026-01-26T14:33:47.5675127Z    |
2026-01-26T14:33:47.5675200Z help: Organize imports
2026-01-26T14:33:47.5675205Z 
2026-01-26T14:33:47.5675311Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5675478Z  --> tests/test_incremental_indexing.py:1:1
2026-01-26T14:33:47.5675538Z   |
2026-01-26T14:33:47.5675612Z 1 | / import unittest
2026-01-26T14:33:47.5675744Z 2 | | from unittest.mock import patch, mock_open, MagicMock
2026-01-26T14:33:47.5675820Z 3 | | from pathlib import Path
2026-01-26T14:33:47.5675895Z 4 | | import json
2026-01-26T14:33:47.5675963Z 5 | | import sys
2026-01-26T14:33:47.5676026Z 6 | | import os
2026-01-26T14:33:47.5676087Z   | |_________^
2026-01-26T14:33:47.5676149Z 7 |
2026-01-26T14:33:47.5676343Z 8 |   sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
2026-01-26T14:33:47.5676402Z   |
2026-01-26T14:33:47.5676472Z help: Organize imports
2026-01-26T14:33:47.5676483Z 
2026-01-26T14:33:47.5676618Z F401 [*] `incremental_indexing.file_lock` imported but unused
2026-01-26T14:33:47.5676722Z   --> tests/test_incremental_indexing.py:10:63
2026-01-26T14:33:47.5676780Z    |
2026-01-26T14:33:47.5676982Z  8 | sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
2026-01-26T14:33:47.5677043Z  9 |
2026-01-26T14:33:47.5677229Z 10 | from incremental_indexing import IndexMetadata, atomic_write, file_lock
2026-01-26T14:33:47.5677333Z    |                                                               ^^^^^^^^^
2026-01-26T14:33:47.5677391Z    |
2026-01-26T14:33:47.5677531Z help: Remove unused import: `incremental_indexing.file_lock`
2026-01-26T14:33:47.5677537Z 
2026-01-26T14:33:47.5677643Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5677740Z  --> tests/test_memory_limited_indexer.py:1:1
2026-01-26T14:33:47.5677799Z   |
2026-01-26T14:33:47.5677869Z 1 | / import unittest
2026-01-26T14:33:47.5678003Z 2 | | from unittest.mock import MagicMock, call
2026-01-26T14:33:47.5678069Z 3 | | import sys
2026-01-26T14:33:47.5678136Z 4 | | import os
2026-01-26T14:33:47.5678202Z   | |_________^
2026-01-26T14:33:47.5678260Z 5 |
2026-01-26T14:33:47.5678468Z 6 |   sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
2026-01-26T14:33:47.5678529Z   |
2026-01-26T14:33:47.5678608Z help: Organize imports
2026-01-26T14:33:47.5678613Z 
2026-01-26T14:33:47.5678720Z F401 [*] `unittest.mock.call` imported but unused
2026-01-26T14:33:47.5679051Z  --> tests/test_memory_limited_indexer.py:2:38
2026-01-26T14:33:47.5679128Z   |
2026-01-26T14:33:47.5679199Z 1 | import unittest
2026-01-26T14:33:47.5679300Z 2 | from unittest.mock import MagicMock, call
2026-01-26T14:33:47.5679373Z   |                                      ^^^^
2026-01-26T14:33:47.5679444Z 3 | import sys
2026-01-26T14:33:47.5679507Z 4 | import os
2026-01-26T14:33:47.5679565Z   |
2026-01-26T14:33:47.5679681Z help: Remove unused import: `unittest.mock.call`
2026-01-26T14:33:47.5679686Z 
2026-01-26T14:33:47.5679772Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5679875Z   --> tests/test_memory_limited_indexer.py:52:1
2026-01-26T14:33:47.5679938Z    |
2026-01-26T14:33:47.5680080Z 50 |         """Test that flush calls the callback with correct data"""
2026-01-26T14:33:47.5680159Z 51 |         received_data = []
2026-01-26T14:33:47.5680221Z 52 |         
2026-01-26T14:33:47.5680285Z    | ^^^^^^^^
2026-01-26T14:33:47.5680386Z 53 |         def capture_callback(docs, metas, ids):
2026-01-26T14:33:47.5680548Z 54 |             received_data.append((docs.copy(), metas.copy(), ids.copy()))
2026-01-26T14:33:47.5680614Z    |
2026-01-26T14:33:47.5680701Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5680706Z 
2026-01-26T14:33:47.5680789Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5680891Z   --> tests/test_memory_limited_indexer.py:55:1
2026-01-26T14:33:47.5680950Z    |
2026-01-26T14:33:47.5681047Z 53 |         def capture_callback(docs, metas, ids):
2026-01-26T14:33:47.5681199Z 54 |             received_data.append((docs.copy(), metas.copy(), ids.copy()))
2026-01-26T14:33:47.5681411Z 55 |         
2026-01-26T14:33:47.5681472Z    | ^^^^^^^^
2026-01-26T14:33:47.5681643Z 56 |         indexer = MemoryLimitedIndexer(self.max_memory, capture_callback)
2026-01-26T14:33:47.5681712Z    |
2026-01-26T14:33:47.5681896Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5681903Z 
2026-01-26T14:33:47.5682070Z F841 Local variable `final_flush_count` is assigned to but never used
2026-01-26T14:33:47.5682180Z    --> tests/test_memory_limited_indexer.py:194:9
2026-01-26T14:33:47.5682239Z     |
2026-01-26T14:33:47.5682318Z 192 |                 indexer.flush()
2026-01-26T14:33:47.5682377Z 193 |
2026-01-26T14:33:47.5682490Z 194 |         final_flush_count = indexer.total_batches
2026-01-26T14:33:47.5682558Z     |         ^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5682639Z 195 |         indexer.flush()
2026-01-26T14:33:47.5682703Z     |
2026-01-26T14:33:47.5682852Z help: Remove assignment to unused variable `final_flush_count`
2026-01-26T14:33:47.5682860Z 
2026-01-26T14:33:47.5682967Z I001 [*] Import block is un-sorted or un-formatted
2026-01-26T14:33:47.5683056Z   --> vector_store_manager.py:1:1
2026-01-26T14:33:47.5683115Z    |
2026-01-26T14:33:47.5683179Z  1 | / import sys
2026-01-26T14:33:47.5683250Z  2 | | import hashlib
2026-01-26T14:33:47.5683318Z  3 | | import json
2026-01-26T14:33:47.5683405Z  4 | | from typing import List, Optional
2026-01-26T14:33:47.5683484Z  5 | | from pathlib import Path
2026-01-26T14:33:47.5683549Z  6 | |
2026-01-26T14:33:47.5683663Z  7 | | from config import VECTOR_STORE_DIR, MODEL_NAME
2026-01-26T14:33:47.5683748Z  8 | | from cache_manager import TTLCache
2026-01-26T14:33:47.5683829Z  9 | | from logger import get_logger
2026-01-26T14:33:47.5683902Z    | |_____________________________^
2026-01-26T14:33:47.5683961Z 10 |
2026-01-26T14:33:47.5684035Z 11 |   logger = get_logger()
2026-01-26T14:33:47.5684098Z    |
2026-01-26T14:33:47.5684170Z help: Organize imports
2026-01-26T14:33:47.5684175Z 
2026-01-26T14:33:47.5684256Z F401 [*] `sys` imported but unused
2026-01-26T14:33:47.5684339Z  --> vector_store_manager.py:1:8
2026-01-26T14:33:47.5684403Z   |
2026-01-26T14:33:47.5684466Z 1 | import sys
2026-01-26T14:33:47.5684526Z   |        ^^^
2026-01-26T14:33:47.5684602Z 2 | import hashlib
2026-01-26T14:33:47.5684667Z 3 | import json
2026-01-26T14:33:47.5684726Z   |
2026-01-26T14:33:47.5684809Z help: Remove unused import: `sys`
2026-01-26T14:33:47.5684814Z 
2026-01-26T14:33:47.5684941Z UP035 `typing.List` is deprecated, use `list` instead
2026-01-26T14:33:47.5685022Z  --> vector_store_manager.py:4:1
2026-01-26T14:33:47.5685080Z   |
2026-01-26T14:33:47.5685154Z 2 | import hashlib
2026-01-26T14:33:47.5685218Z 3 | import json
2026-01-26T14:33:47.5685303Z 4 | from typing import List, Optional
2026-01-26T14:33:47.5685379Z   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5685459Z 5 | from pathlib import Path
2026-01-26T14:33:47.5685517Z   |
2026-01-26T14:33:47.5685522Z 
2026-01-26T14:33:47.5685618Z F401 [*] `pathlib.Path` imported but unused
2026-01-26T14:33:47.5685711Z  --> vector_store_manager.py:5:21
2026-01-26T14:33:47.5685771Z   |
2026-01-26T14:33:47.5685835Z 3 | import json
2026-01-26T14:33:47.5685920Z 4 | from typing import List, Optional
2026-01-26T14:33:47.5685999Z 5 | from pathlib import Path
2026-01-26T14:33:47.5686064Z   |                     ^^^^
2026-01-26T14:33:47.5686123Z 6 |
2026-01-26T14:33:47.5686237Z 7 | from config import VECTOR_STORE_DIR, MODEL_NAME
2026-01-26T14:33:47.5686296Z   |
2026-01-26T14:33:47.5686394Z help: Remove unused import: `pathlib.Path`
2026-01-26T14:33:47.5686399Z 
2026-01-26T14:33:47.5686491Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5686575Z   --> vector_store_manager.py:19:1
2026-01-26T14:33:47.5686633Z    |
2026-01-26T14:33:47.5686816Z 17 |     Encapsulates client, collection, and embedding function management.
2026-01-26T14:33:47.5686878Z 18 |     """
2026-01-26T14:33:47.5686938Z 19 |     
2026-01-26T14:33:47.5686997Z    | ^^^^
2026-01-26T14:33:47.5687246Z 20 |     def __init__(self, collection_name: str = "project_codebase"):
2026-01-26T14:33:47.5687308Z 21 |         """
2026-01-26T14:33:47.5687367Z    |
2026-01-26T14:33:47.5687460Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5687465Z 
2026-01-26T14:33:47.5687618Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5687702Z   --> vector_store_manager.py:23:1
2026-01-26T14:33:47.5687762Z    |
2026-01-26T14:33:47.5687829Z 21 |         """
2026-01-26T14:33:47.5687921Z 22 |         Initialize vector store manager.
2026-01-26T14:33:47.5687982Z 23 |         
2026-01-26T14:33:47.5688046Z    | ^^^^^^^^
2026-01-26T14:33:47.5688109Z 24 |         Args:
2026-01-26T14:33:47.5688235Z 25 |             collection_name: Name of the ChromaDB collection
2026-01-26T14:33:47.5688295Z    |
2026-01-26T14:33:47.5688387Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5688392Z 
2026-01-26T14:33:47.5688475Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5688557Z   --> vector_store_manager.py:33:1
2026-01-26T14:33:47.5688624Z    |
2026-01-26T14:33:47.5688704Z 31 |         self._initialized = False
2026-01-26T14:33:47.5688966Z 32 |         self._query_cache = TTLCache(ttl_seconds=300, max_size=100)
2026-01-26T14:33:47.5689034Z 33 |     
2026-01-26T14:33:47.5689099Z    | ^^^^
2026-01-26T14:33:47.5689183Z 34 |     def initialize(self) -> bool:
2026-01-26T14:33:47.5689244Z 35 |         """
2026-01-26T14:33:47.5689310Z    |
2026-01-26T14:33:47.5689396Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5689401Z 
2026-01-26T14:33:47.5689482Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5689568Z   --> vector_store_manager.py:37:1
2026-01-26T14:33:47.5689630Z    |
2026-01-26T14:33:47.5689690Z 35 |         """
2026-01-26T14:33:47.5689859Z 36 |         Initializes ChromaDB client, embedding function, and collection.
2026-01-26T14:33:47.5689925Z 37 |         
2026-01-26T14:33:47.5689985Z    | ^^^^^^^^
2026-01-26T14:33:47.5690050Z 38 |         Returns:
2026-01-26T14:33:47.5690186Z 39 |             True if initialization successful, False otherwise
2026-01-26T14:33:47.5690248Z    |
2026-01-26T14:33:47.5690333Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5690337Z 
2026-01-26T14:33:47.5690423Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5690504Z   --> vector_store_manager.py:43:1
2026-01-26T14:33:47.5690563Z    |
2026-01-26T14:33:47.5690697Z 41 |         if self._initialized and self.collection is not None:
2026-01-26T14:33:47.5690773Z 42 |             return True
2026-01-26T14:33:47.5690833Z 43 |         
2026-01-26T14:33:47.5690895Z    | ^^^^^^^^
2026-01-26T14:33:47.5691014Z 44 |         logger.info("Initializing Vector Store...")
2026-01-26T14:33:47.5691073Z    |
2026-01-26T14:33:47.5691158Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5691163Z 
2026-01-26T14:33:47.5691245Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5691328Z   --> vector_store_manager.py:45:1
2026-01-26T14:33:47.5691387Z    |
2026-01-26T14:33:47.5691495Z 44 |         logger.info("Initializing Vector Store...")
2026-01-26T14:33:47.5691564Z 45 |         
2026-01-26T14:33:47.5691624Z    | ^^^^^^^^
2026-01-26T14:33:47.5691686Z 46 |         try:
2026-01-26T14:33:47.5691766Z 47 |             import chromadb
2026-01-26T14:33:47.5691830Z    |
2026-01-26T14:33:47.5691916Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5691921Z 
2026-01-26T14:33:47.5692001Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5692086Z   --> vector_store_manager.py:50:1
2026-01-26T14:33:47.5692144Z    |
2026-01-26T14:33:47.5692267Z 48 |             from chromadb.utils import embedding_functions
2026-01-26T14:33:47.5692411Z 49 |             from sentence_transformers import SentenceTransformer
2026-01-26T14:33:47.5692472Z 50 |             
2026-01-26T14:33:47.5692534Z    | ^^^^^^^^^^^^
2026-01-26T14:33:47.5692823Z 51 |             class LocalSentenceTransformerEmbeddingFunction(embedding_functions.EmbeddingFunction):
2026-01-26T14:33:47.5692949Z 52 |                 def __init__(self, model_name: str) -> None:
2026-01-26T14:33:47.5693129Z    |
2026-01-26T14:33:47.5693217Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5693223Z 
2026-01-26T14:33:47.5693309Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5693493Z   --> vector_store_manager.py:54:1
2026-01-26T14:33:47.5693557Z    |
2026-01-26T14:33:47.5693675Z 52 |                 def __init__(self, model_name: str) -> None:
2026-01-26T14:33:47.5693801Z 53 |                     self.model = SentenceTransformer(model_name)
2026-01-26T14:33:47.5693867Z 54 |                 
2026-01-26T14:33:47.5693931Z    | ^^^^^^^^^^^^^^^^
2026-01-26T14:33:47.5694081Z 55 |                 def __call__(self, input: List[str]) -> List[List[float]]:
2026-01-26T14:33:47.5694197Z 56 |                     return self.model.encode(input).tolist()
2026-01-26T14:33:47.5694255Z    |
2026-01-26T14:33:47.5694345Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5694350Z 
2026-01-26T14:33:47.5694475Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5694563Z   --> vector_store_manager.py:55:43
2026-01-26T14:33:47.5694627Z    |
2026-01-26T14:33:47.5694748Z 53 |                     self.model = SentenceTransformer(model_name)
2026-01-26T14:33:47.5694813Z 54 |                 
2026-01-26T14:33:47.5694959Z 55 |                 def __call__(self, input: List[str]) -> List[List[float]]:
2026-01-26T14:33:47.5695047Z    |                                           ^^^^
2026-01-26T14:33:47.5695159Z 56 |                     return self.model.encode(input).tolist()
2026-01-26T14:33:47.5695218Z    |
2026-01-26T14:33:47.5695301Z help: Replace with `list`
2026-01-26T14:33:47.5695306Z 
2026-01-26T14:33:47.5695427Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5695509Z   --> vector_store_manager.py:55:57
2026-01-26T14:33:47.5695572Z    |
2026-01-26T14:33:47.5695693Z 53 |                     self.model = SentenceTransformer(model_name)
2026-01-26T14:33:47.5695760Z 54 |                 
2026-01-26T14:33:47.5695915Z 55 |                 def __call__(self, input: List[str]) -> List[List[float]]:
2026-01-26T14:33:47.5696006Z    |                                                         ^^^^
2026-01-26T14:33:47.5696117Z 56 |                     return self.model.encode(input).tolist()
2026-01-26T14:33:47.5696177Z    |
2026-01-26T14:33:47.5696260Z help: Replace with `list`
2026-01-26T14:33:47.5696266Z 
2026-01-26T14:33:47.5696383Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5696465Z   --> vector_store_manager.py:55:62
2026-01-26T14:33:47.5696530Z    |
2026-01-26T14:33:47.5696649Z 53 |                     self.model = SentenceTransformer(model_name)
2026-01-26T14:33:47.5696712Z 54 |                 
2026-01-26T14:33:47.5696850Z 55 |                 def __call__(self, input: List[str]) -> List[List[float]]:
2026-01-26T14:33:47.5696945Z    |                                                              ^^^^
2026-01-26T14:33:47.5697055Z 56 |                     return self.model.encode(input).tolist()
2026-01-26T14:33:47.5697127Z    |
2026-01-26T14:33:47.5697219Z help: Replace with `list`
2026-01-26T14:33:47.5697224Z 
2026-01-26T14:33:47.5697307Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5697391Z   --> vector_store_manager.py:57:1
2026-01-26T14:33:47.5697459Z    |
2026-01-26T14:33:47.5697594Z 55 |                 def __call__(self, input: List[str]) -> List[List[float]]:
2026-01-26T14:33:47.5697704Z 56 |                     return self.model.encode(input).tolist()
2026-01-26T14:33:47.5697770Z 57 |             
2026-01-26T14:33:47.5697832Z    | ^^^^^^^^^^^^
2026-01-26T14:33:47.5698047Z 58 |             self.chroma_client = chromadb.PersistentClient(path=str(VECTOR_STORE_DIR))
2026-01-26T14:33:47.5698271Z 59 |             self.embedding_fn = LocalSentenceTransformerEmbeddingFunction(MODEL_NAME)
2026-01-26T14:33:47.5698335Z    |
2026-01-26T14:33:47.5698429Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5698434Z 
2026-01-26T14:33:47.5698517Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5698690Z   --> vector_store_manager.py:64:1
2026-01-26T14:33:47.5698750Z    |
2026-01-26T14:33:47.5698956Z 62 |                 embedding_function=self.embedding_fn
2026-01-26T14:33:47.5699023Z 63 |             )
2026-01-26T14:33:47.5699196Z 64 |             
2026-01-26T14:33:47.5699261Z    | ^^^^^^^^^^^^
2026-01-26T14:33:47.5699347Z 65 |             self._initialized = True
2026-01-26T14:33:47.5699492Z 66 |             logger.info("Vector Store initialized successfully")
2026-01-26T14:33:47.5699552Z    |
2026-01-26T14:33:47.5699636Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5699642Z 
2026-01-26T14:33:47.5699729Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5699811Z   --> vector_store_manager.py:71:1
2026-01-26T14:33:47.5699870Z    |
2026-01-26T14:33:47.5700038Z 69 |             logger.error(f"Failed to initialize ChromaDB: {e}", exc_info=True)
2026-01-26T14:33:47.5700118Z 70 |             return False
2026-01-26T14:33:47.5700181Z 71 |     
2026-01-26T14:33:47.5700255Z    | ^^^^
2026-01-26T14:33:47.5700337Z 72 |     def get_collection(self):
2026-01-26T14:33:47.5700399Z 73 |         """
2026-01-26T14:33:47.5700458Z    |
2026-01-26T14:33:47.5700547Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5700556Z 
2026-01-26T14:33:47.5700637Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5700718Z   --> vector_store_manager.py:75:1
2026-01-26T14:33:47.5700777Z    |
2026-01-26T14:33:47.5700842Z 73 |         """
2026-01-26T14:33:47.5700954Z 74 |         Gets the collection, initializing if needed.
2026-01-26T14:33:47.5701013Z 75 |         
2026-01-26T14:33:47.5701077Z    | ^^^^^^^^
2026-01-26T14:33:47.5701141Z 76 |         Returns:
2026-01-26T14:33:47.5701273Z 77 |             ChromaDB collection or None if initialization failed
2026-01-26T14:33:47.5701331Z    |
2026-01-26T14:33:47.5701420Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5701425Z 
2026-01-26T14:33:47.5701505Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5701588Z   --> vector_store_manager.py:83:1
2026-01-26T14:33:47.5701653Z    |
2026-01-26T14:33:47.5701724Z 81 |                 return None
2026-01-26T14:33:47.5701800Z 82 |         return self.collection
2026-01-26T14:33:47.5701869Z 83 |     
2026-01-26T14:33:47.5701929Z    | ^^^^
2026-01-26T14:33:47.5702041Z 84 |     def clear_collection(self) -> Optional[str]:
2026-01-26T14:33:47.5702103Z 85 |         """
2026-01-26T14:33:47.5702169Z    |
2026-01-26T14:33:47.5702254Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5702260Z 
2026-01-26T14:33:47.5702354Z UP045 [*] Use `X | None` for type annotations
2026-01-26T14:33:47.5702439Z   --> vector_store_manager.py:84:35
2026-01-26T14:33:47.5702498Z    |
2026-01-26T14:33:47.5702572Z 82 |         return self.collection
2026-01-26T14:33:47.5702632Z 83 |     
2026-01-26T14:33:47.5702745Z 84 |     def clear_collection(self) -> Optional[str]:
2026-01-26T14:33:47.5702828Z    |                                   ^^^^^^^^^^^^^
2026-01-26T14:33:47.5702892Z 85 |         """
2026-01-26T14:33:47.5703052Z 86 |         Clears the current collection by deleting and recreating it.
2026-01-26T14:33:47.5703112Z    |
2026-01-26T14:33:47.5703189Z help: Convert to `X | None`
2026-01-26T14:33:47.5703194Z 
2026-01-26T14:33:47.5703281Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5703369Z   --> vector_store_manager.py:87:1
2026-01-26T14:33:47.5703428Z    |
2026-01-26T14:33:47.5703488Z 85 |         """
2026-01-26T14:33:47.5703639Z 86 |         Clears the current collection by deleting and recreating it.
2026-01-26T14:33:47.5703701Z 87 |         
2026-01-26T14:33:47.5703760Z    | ^^^^^^^^
2026-01-26T14:33:47.5703829Z 88 |         Returns:
2026-01-26T14:33:47.5703955Z 89 |             Error message if failed, None if successful
2026-01-26T14:33:47.5704018Z    |
2026-01-26T14:33:47.5704107Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5704113Z 
2026-01-26T14:33:47.5704198Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5704396Z   --> vector_store_manager.py:93:1
2026-01-26T14:33:47.5704455Z    |
2026-01-26T14:33:47.5704541Z 91 |         if not self.chroma_client:
2026-01-26T14:33:47.5704645Z 92 |             return "ChromaDB client not initialized"
2026-01-26T14:33:47.5704794Z 93 |         
2026-01-26T14:33:47.5704868Z    | ^^^^^^^^
2026-01-26T14:33:47.5704931Z 94 |         try:
2026-01-26T14:33:47.5705085Z 95 |             self.chroma_client.delete_collection(self.collection_name)
2026-01-26T14:33:47.5705143Z    |
2026-01-26T14:33:47.5705233Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5705239Z 
2026-01-26T14:33:47.5705319Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5705405Z    --> vector_store_manager.py:106:1
2026-01-26T14:33:47.5705470Z     |
2026-01-26T14:33:47.5705554Z 104 |             logger.error(error_msg)
2026-01-26T14:33:47.5705625Z 105 |             return error_msg
2026-01-26T14:33:47.5705685Z 106 |     
2026-01-26T14:33:47.5705750Z     | ^^^^
2026-01-26T14:33:47.5705865Z 107 |     def get_count(self) -> Optional[int]:
2026-01-26T14:33:47.5705926Z 108 |         """
2026-01-26T14:33:47.5705992Z     |
2026-01-26T14:33:47.5706076Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5706081Z 
2026-01-26T14:33:47.5706177Z UP045 [*] Use `X | None` for type annotations
2026-01-26T14:33:47.5706269Z    --> vector_store_manager.py:107:28
2026-01-26T14:33:47.5706327Z     |
2026-01-26T14:33:47.5706399Z 105 |             return error_msg
2026-01-26T14:33:47.5706458Z 106 |     
2026-01-26T14:33:47.5706555Z 107 |     def get_count(self) -> Optional[int]:
2026-01-26T14:33:47.5706632Z     |                            ^^^^^^^^^^^^^
2026-01-26T14:33:47.5706693Z 108 |         """
2026-01-26T14:33:47.5706809Z 109 |         Gets the number of items in the collection.
2026-01-26T14:33:47.5706869Z     |
2026-01-26T14:33:47.5706943Z help: Convert to `X | None`
2026-01-26T14:33:47.5706948Z 
2026-01-26T14:33:47.5707027Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5707113Z    --> vector_store_manager.py:110:1
2026-01-26T14:33:47.5707175Z     |
2026-01-26T14:33:47.5707235Z 108 |         """
2026-01-26T14:33:47.5707348Z 109 |         Gets the number of items in the collection.
2026-01-26T14:33:47.5707410Z 110 |         
2026-01-26T14:33:47.5707472Z     | ^^^^^^^^
2026-01-26T14:33:47.5707538Z 111 |         Returns:
2026-01-26T14:33:47.5707683Z 112 |             Number of items, or None if collection not initialized
2026-01-26T14:33:47.5707743Z     |
2026-01-26T14:33:47.5707830Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5707835Z 
2026-01-26T14:33:47.5707922Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5708002Z    --> vector_store_manager.py:117:1
2026-01-26T14:33:47.5708061Z     |
2026-01-26T14:33:47.5708138Z 115 |         if coll is None:
2026-01-26T14:33:47.5708208Z 116 |             return None
2026-01-26T14:33:47.5708270Z 117 |         
2026-01-26T14:33:47.5708330Z     | ^^^^^^^^
2026-01-26T14:33:47.5708396Z 118 |         try:
2026-01-26T14:33:47.5708478Z 119 |             return coll.count()
2026-01-26T14:33:47.5708537Z     |
2026-01-26T14:33:47.5708625Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5708630Z 
2026-01-26T14:33:47.5708710Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5708895Z    --> vector_store_manager.py:123:1
2026-01-26T14:33:47.5708962Z     |
2026-01-26T14:33:47.5709101Z 121 |             logger.error(f"Error getting collection count: {e}")
2026-01-26T14:33:47.5709173Z 122 |             return None
2026-01-26T14:33:47.5709233Z 123 |     
2026-01-26T14:33:47.5709298Z     | ^^^^
2026-01-26T14:33:47.5709363Z 124 |     def query(
2026-01-26T14:33:47.5709426Z 125 |         self,
2026-01-26T14:33:47.5709490Z     |
2026-01-26T14:33:47.5709577Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5709583Z 
2026-01-26T14:33:47.5709710Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5709794Z    --> vector_store_manager.py:126:22
2026-01-26T14:33:47.5709859Z     |
2026-01-26T14:33:47.5710106Z 124 |     def query(
2026-01-26T14:33:47.5710169Z 125 |         self,
2026-01-26T14:33:47.5710252Z 126 |         query_texts: List[str],
2026-01-26T14:33:47.5710320Z     |                      ^^^^
2026-01-26T14:33:47.5710395Z 127 |         n_results: int = 5,
2026-01-26T14:33:47.5710581Z 128 |         where: Optional[dict] = None,
2026-01-26T14:33:47.5710649Z     |
2026-01-26T14:33:47.5710726Z help: Replace with `list`
2026-01-26T14:33:47.5710731Z 
2026-01-26T14:33:47.5710828Z UP045 [*] Use `X | None` for type annotations
2026-01-26T14:33:47.5710916Z    --> vector_store_manager.py:128:16
2026-01-26T14:33:47.5710974Z     |
2026-01-26T14:33:47.5711050Z 126 |         query_texts: List[str],
2026-01-26T14:33:47.5711128Z 127 |         n_results: int = 5,
2026-01-26T14:33:47.5711212Z 128 |         where: Optional[dict] = None,
2026-01-26T14:33:47.5711280Z     |                ^^^^^^^^^^^^^^
2026-01-26T14:33:47.5711381Z 129 |         where_document: Optional[dict] = None
2026-01-26T14:33:47.5711462Z 130 |     ) -> Optional[dict]:
2026-01-26T14:33:47.5711524Z     |
2026-01-26T14:33:47.5711599Z help: Convert to `X | None`
2026-01-26T14:33:47.5711604Z 
2026-01-26T14:33:47.5711702Z UP045 [*] Use `X | None` for type annotations
2026-01-26T14:33:47.5711786Z    --> vector_store_manager.py:129:25
2026-01-26T14:33:47.5711845Z     |
2026-01-26T14:33:47.5711922Z 127 |         n_results: int = 5,
2026-01-26T14:33:47.5712005Z 128 |         where: Optional[dict] = None,
2026-01-26T14:33:47.5712101Z 129 |         where_document: Optional[dict] = None
2026-01-26T14:33:47.5712179Z     |                         ^^^^^^^^^^^^^^
2026-01-26T14:33:47.5712261Z 130 |     ) -> Optional[dict]:
2026-01-26T14:33:47.5712323Z 131 |         """
2026-01-26T14:33:47.5712382Z     |
2026-01-26T14:33:47.5712460Z help: Convert to `X | None`
2026-01-26T14:33:47.5712465Z 
2026-01-26T14:33:47.5712555Z UP045 [*] Use `X | None` for type annotations
2026-01-26T14:33:47.5712636Z    --> vector_store_manager.py:130:10
2026-01-26T14:33:47.5712695Z     |
2026-01-26T14:33:47.5712793Z 128 |         where: Optional[dict] = None,
2026-01-26T14:33:47.5712887Z 129 |         where_document: Optional[dict] = None
2026-01-26T14:33:47.5712961Z 130 |     ) -> Optional[dict]:
2026-01-26T14:33:47.5713034Z     |          ^^^^^^^^^^^^^^
2026-01-26T14:33:47.5713099Z 131 |         """
2026-01-26T14:33:47.5713209Z 132 |         Queries the vector store with caching.
2026-01-26T14:33:47.5713282Z     |
2026-01-26T14:33:47.5713357Z help: Convert to `X | None`
2026-01-26T14:33:47.5713362Z 
2026-01-26T14:33:47.5713442Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5713538Z    --> vector_store_manager.py:133:1
2026-01-26T14:33:47.5713609Z     |
2026-01-26T14:33:47.5713669Z 131 |         """
2026-01-26T14:33:47.5713768Z 132 |         Queries the vector store with caching.
2026-01-26T14:33:47.5713835Z 133 |         
2026-01-26T14:33:47.5713896Z     | ^^^^^^^^
2026-01-26T14:33:47.5713960Z 134 |         Args:
2026-01-26T14:33:47.5714053Z 135 |             query_texts: List of query strings
2026-01-26T14:33:47.5714120Z     |
2026-01-26T14:33:47.5714209Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5714213Z 
2026-01-26T14:33:47.5714292Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5714382Z    --> vector_store_manager.py:139:1
2026-01-26T14:33:47.5714442Z     |
2026-01-26T14:33:47.5714536Z 137 |             where: Optional metadata filter
2026-01-26T14:33:47.5714683Z 138 |             where_document: Optional document content filter
2026-01-26T14:33:47.5714745Z 139 |             
2026-01-26T14:33:47.5714805Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5714871Z 140 |         Returns:
2026-01-26T14:33:47.5714979Z 141 |             Query results or None if query failed
2026-01-26T14:33:47.5715038Z     |
2026-01-26T14:33:47.5715125Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5715130Z 
2026-01-26T14:33:47.5715216Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5715296Z    --> vector_store_manager.py:148:1
2026-01-26T14:33:47.5715354Z     |
2026-01-26T14:33:47.5715618Z 146 |             logger.debug(f"Cache hit for query: {query_texts[0][:50]}...")
2026-01-26T14:33:47.5715704Z 147 |             return cached_result
2026-01-26T14:33:47.5715765Z 148 |         
2026-01-26T14:33:47.5715833Z     | ^^^^^^^^
2026-01-26T14:33:47.5715997Z 149 |         coll = self.get_collection()
2026-01-26T14:33:47.5716069Z 150 |         if coll is None:
2026-01-26T14:33:47.5716129Z     |
2026-01-26T14:33:47.5716218Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5716223Z 
2026-01-26T14:33:47.5716303Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5716385Z    --> vector_store_manager.py:152:1
2026-01-26T14:33:47.5716447Z     |
2026-01-26T14:33:47.5716524Z 150 |         if coll is None:
2026-01-26T14:33:47.5716594Z 151 |             return None
2026-01-26T14:33:47.5716655Z 152 |         
2026-01-26T14:33:47.5716720Z     | ^^^^^^^^
2026-01-26T14:33:47.5716782Z 153 |         try:
2026-01-26T14:33:47.5716860Z 154 |             result = coll.query(
2026-01-26T14:33:47.5716997Z     |
2026-01-26T14:33:47.5717158Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5717166Z 
2026-01-26T14:33:47.5717300Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5717472Z    --> vector_store_manager.py:165:1
2026-01-26T14:33:47.5717579Z     |
2026-01-26T14:33:47.5717839Z 163 |             logger.error(f"Error querying collection: {e}", exc_info=True)
2026-01-26T14:33:47.5717957Z 164 |             return None
2026-01-26T14:33:47.5718066Z 165 |     
2026-01-26T14:33:47.5718157Z     | ^^^^
2026-01-26T14:33:47.5718289Z 166 |     def _generate_cache_key(
2026-01-26T14:33:47.5718390Z 167 |         self,
2026-01-26T14:33:47.5718501Z     |
2026-01-26T14:33:47.5718654Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5718663Z 
2026-01-26T14:33:47.5719009Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5719163Z    --> vector_store_manager.py:168:22
2026-01-26T14:33:47.5719262Z     |
2026-01-26T14:33:47.5719391Z 166 |     def _generate_cache_key(
2026-01-26T14:33:47.5719502Z 167 |         self,
2026-01-26T14:33:47.5719634Z 168 |         query_texts: List[str],
2026-01-26T14:33:47.5719749Z     |                      ^^^^
2026-01-26T14:33:47.5719871Z 169 |         n_results: int,
2026-01-26T14:33:47.5720012Z 170 |         where: Optional[dict],
2026-01-26T14:33:47.5720115Z     |
2026-01-26T14:33:47.5720243Z help: Replace with `list`
2026-01-26T14:33:47.5720250Z 
2026-01-26T14:33:47.5720411Z UP045 [*] Use `X | None` for type annotations
2026-01-26T14:33:47.5720550Z    --> vector_store_manager.py:170:16
2026-01-26T14:33:47.5720649Z     |
2026-01-26T14:33:47.5720773Z 168 |         query_texts: List[str],
2026-01-26T14:33:47.5720884Z 169 |         n_results: int,
2026-01-26T14:33:47.5721008Z 170 |         where: Optional[dict],
2026-01-26T14:33:47.5721111Z     |                ^^^^^^^^^^^^^^
2026-01-26T14:33:47.5721260Z 171 |         where_document: Optional[dict]
2026-01-26T14:33:47.5721358Z 172 |     ) -> str:
2026-01-26T14:33:47.5721456Z     |
2026-01-26T14:33:47.5721572Z help: Convert to `X | None`
2026-01-26T14:33:47.5721580Z 
2026-01-26T14:33:47.5721731Z UP045 [*] Use `X | None` for type annotations
2026-01-26T14:33:47.5722019Z    --> vector_store_manager.py:171:25
2026-01-26T14:33:47.5722132Z     |
2026-01-26T14:33:47.5722251Z 169 |         n_results: int,
2026-01-26T14:33:47.5722362Z 170 |         where: Optional[dict],
2026-01-26T14:33:47.5722501Z 171 |         where_document: Optional[dict]
2026-01-26T14:33:47.5722626Z     |                         ^^^^^^^^^^^^^^
2026-01-26T14:33:47.5722730Z 172 |     ) -> str:
2026-01-26T14:33:47.5722835Z 173 |         """
2026-01-26T14:33:47.5722931Z     |
2026-01-26T14:33:47.5723057Z help: Convert to `X | None`
2026-01-26T14:33:47.5723066Z 
2026-01-26T14:33:47.5723208Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5723352Z    --> vector_store_manager.py:175:1
2026-01-26T14:33:47.5723460Z     |
2026-01-26T14:33:47.5723562Z 173 |         """
2026-01-26T14:33:47.5723792Z 174 |         Generates a unique cache key for query parameters.
2026-01-26T14:33:47.5724105Z 175 |         
2026-01-26T14:33:47.5724215Z     | ^^^^^^^^
2026-01-26T14:33:47.5724321Z 176 |         Args:
2026-01-26T14:33:47.5724630Z 177 |             query_texts: List of query strings
2026-01-26T14:33:47.5724738Z     |
2026-01-26T14:33:47.5724889Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5724898Z 
2026-01-26T14:33:47.5725035Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5725184Z    --> vector_store_manager.py:181:1
2026-01-26T14:33:47.5725286Z     |
2026-01-26T14:33:47.5725423Z 179 |             where: Metadata filter
2026-01-26T14:33:47.5725593Z 180 |             where_document: Document filter
2026-01-26T14:33:47.5725704Z 181 |             
2026-01-26T14:33:47.5725806Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5725917Z 182 |         Returns:
2026-01-26T14:33:47.5726066Z 183 |             Hash string for cache key
2026-01-26T14:33:47.5726166Z     |
2026-01-26T14:33:47.5726314Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5726331Z 
2026-01-26T14:33:47.5726474Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5726617Z    --> vector_store_manager.py:193:1
2026-01-26T14:33:47.5726715Z     |
2026-01-26T14:33:47.5726924Z 191 |         key_str = json.dumps(key_data, sort_keys=True)
2026-01-26T14:33:47.5727160Z 192 |         return hashlib.sha256(key_str.encode()).hexdigest()
2026-01-26T14:33:47.5727262Z 193 |     
2026-01-26T14:33:47.5727361Z     | ^^^^
2026-01-26T14:33:47.5727516Z 194 |     def get_query_cache_stats(self):
2026-01-26T14:33:47.5727617Z 195 |         """
2026-01-26T14:33:47.5727716Z     |
2026-01-26T14:33:47.5727872Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5727880Z 
2026-01-26T14:33:47.5728020Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5728154Z    --> vector_store_manager.py:197:1
2026-01-26T14:33:47.5728253Z     |
2026-01-26T14:33:47.5728361Z 195 |         """
2026-01-26T14:33:47.5728521Z 196 |         Returns query cache statistics.
2026-01-26T14:33:47.5728631Z 197 |         
2026-01-26T14:33:47.5728732Z     | ^^^^^^^^
2026-01-26T14:33:47.5729595Z 198 |         Returns:
2026-01-26T14:33:47.5729784Z 199 |             Dictionary with cache statistics
2026-01-26T14:33:47.5729885Z     |
2026-01-26T14:33:47.5730050Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5730059Z 
2026-01-26T14:33:47.5730199Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5730340Z    --> vector_store_manager.py:202:1
2026-01-26T14:33:47.5730445Z     |
2026-01-26T14:33:47.5730548Z 200 |         """
2026-01-26T14:33:47.5730713Z 201 |         return self._query_cache.get_stats()
2026-01-26T14:33:47.5730816Z 202 |     
2026-01-26T14:33:47.5730920Z     | ^^^^
2026-01-26T14:33:47.5731033Z 203 |     def upsert(
2026-01-26T14:33:47.5731137Z 204 |         self,
2026-01-26T14:33:47.5731241Z     |
2026-01-26T14:33:47.5731389Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5731397Z 
2026-01-26T14:33:47.5731612Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5731762Z    --> vector_store_manager.py:205:20
2026-01-26T14:33:47.5731866Z     |
2026-01-26T14:33:47.5731977Z 203 |     def upsert(
2026-01-26T14:33:47.5732080Z 204 |         self,
2026-01-26T14:33:47.5732219Z 205 |         documents: List[str],
2026-01-26T14:33:47.5732331Z     |                    ^^^^
2026-01-26T14:33:47.5732460Z 206 |         metadatas: List[dict],
2026-01-26T14:33:47.5732577Z 207 |         ids: List[str]
2026-01-26T14:33:47.5732682Z     |
2026-01-26T14:33:47.5732809Z help: Replace with `list`
2026-01-26T14:33:47.5732817Z 
2026-01-26T14:33:47.5733026Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5733173Z    --> vector_store_manager.py:206:20
2026-01-26T14:33:47.5733272Z     |
2026-01-26T14:33:47.5733374Z 204 |         self,
2026-01-26T14:33:47.5733504Z 205 |         documents: List[str],
2026-01-26T14:33:47.5733629Z 206 |         metadatas: List[dict],
2026-01-26T14:33:47.5733742Z     |                    ^^^^
2026-01-26T14:33:47.5734041Z 207 |         ids: List[str]
2026-01-26T14:33:47.5734158Z 208 |     ) -> bool:
2026-01-26T14:33:47.5734256Z     |
2026-01-26T14:33:47.5734381Z help: Replace with `list`
2026-01-26T14:33:47.5734388Z 
2026-01-26T14:33:47.5734729Z UP006 [*] Use `list` instead of `List` for type annotation
2026-01-26T14:33:47.5734871Z    --> vector_store_manager.py:207:14
2026-01-26T14:33:47.5734970Z     |
2026-01-26T14:33:47.5735098Z 205 |         documents: List[str],
2026-01-26T14:33:47.5735234Z 206 |         metadatas: List[dict],
2026-01-26T14:33:47.5735348Z 207 |         ids: List[str]
2026-01-26T14:33:47.5735456Z     |              ^^^^
2026-01-26T14:33:47.5735569Z 208 |     ) -> bool:
2026-01-26T14:33:47.5735671Z 209 |         """
2026-01-26T14:33:47.5735769Z     |
2026-01-26T14:33:47.5735894Z help: Replace with `list`
2026-01-26T14:33:47.5735909Z 
2026-01-26T14:33:47.5736046Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5736185Z    --> vector_store_manager.py:211:1
2026-01-26T14:33:47.5736290Z     |
2026-01-26T14:33:47.5736398Z 209 |         """
2026-01-26T14:33:47.5736576Z 210 |         Upserts documents into the collection.
2026-01-26T14:33:47.5736678Z 211 |         
2026-01-26T14:33:47.5736785Z     | ^^^^^^^^
2026-01-26T14:33:47.5736892Z 212 |         Args:
2026-01-26T14:33:47.5737059Z 213 |             documents: List of document texts
2026-01-26T14:33:47.5737158Z     |
2026-01-26T14:33:47.5737311Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5737319Z 
2026-01-26T14:33:47.5737456Z W293 Blank line contains whitespace
2026-01-26T14:33:47.5737594Z    --> vector_store_manager.py:216:1
2026-01-26T14:33:47.5737701Z     |
2026-01-26T14:33:47.5737861Z 214 |             metadatas: List of metadata dicts
2026-01-26T14:33:47.5738001Z 215 |             ids: List of document IDs
2026-01-26T14:33:47.5738099Z 216 |             
2026-01-26T14:33:47.5738201Z     | ^^^^^^^^^^^^
2026-01-26T14:33:47.5738295Z 217 |         Returns:
2026-01-26T14:33:47.5738462Z 218 |             True if successful, False otherwise
2026-01-26T14:33:47.5738568Z     |
2026-01-26T14:33:47.5738710Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5738719Z 
2026-01-26T14:33:47.5739032Z W293 [*] Blank line contains whitespace
2026-01-26T14:33:47.5739178Z    --> vector_store_manager.py:223:1
2026-01-26T14:33:47.5739281Z     |
2026-01-26T14:33:47.5739400Z 221 |         if coll is None:
2026-01-26T14:33:47.5739520Z 222 |             return False
2026-01-26T14:33:47.5739622Z 223 |         
2026-01-26T14:33:47.5739721Z     | ^^^^^^^^
2026-01-26T14:33:47.5739829Z 224 |         try:
2026-01-26T14:33:47.5739943Z 225 |             coll.upsert(
2026-01-26T14:33:47.5740036Z     |
2026-01-26T14:33:47.5740175Z help: Remove whitespace from blank line
2026-01-26T14:33:47.5740185Z 
2026-01-26T14:33:47.5740294Z Found 719 errors.
2026-01-26T14:33:47.5740794Z [*] 605 fixable with the `--fix` option (79 hidden fixes can be enabled with the `--unsafe-fixes` option).
2026-01-26T14:33:47.5752302Z ##[error]Process completed with exit code 1.
2026-01-26T14:33:47.5896945Z Post job cleanup.
2026-01-26T14:33:47.8387310Z [command]/usr/bin/git version
2026-01-26T14:33:47.8476419Z git version 2.52.0
2026-01-26T14:33:47.8564583Z Temporarily overriding HOME='/home/runner/work/_temp/19cf422a-5cca-456e-8de4-80f211794177' before making global git config changes
2026-01-26T14:33:47.8567656Z Adding repository directory to the temporary git global config as a safe directory
2026-01-26T14:33:47.8577393Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/ProjectMindMCP/ProjectMindMCP
2026-01-26T14:33:47.8669890Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-01-26T14:33:47.8729284Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-01-26T14:33:47.9217942Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-01-26T14:33:47.9269057Z http.https://github.com/.extraheader
2026-01-26T14:33:47.9294323Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
2026-01-26T14:33:47.9356202Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-01-26T14:33:47.9747465Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-01-26T14:33:47.9813281Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-01-26T14:33:48.0224541Z Cleaning up orphan processes