**Docker Storage**

Docker keeps everything in */var/lib/docker* (main folder).

Inside it:

* images/ - docker images
* containers/ - running container data
* volumes/ - persistent data(imp)
* overlay2/ - layered filesystem data



**Docker Layer System**

Docker images are made of layers:

* Each Dockerfile line = one layer
* Each layer only stores changes.
* Layers are read-only.

When container runs:

* Docker adds a new writable layer on top
* Any changes you may go there

This is called Copy-on-Write

* Original image stays same
* Changes are stored separately



**Layer Reuse**

* If two images have same steps - Docker reuses layers
* Saves time+disk space



**Persistent Data Problem**

Problem:

* Container data is temporary.
* If container is deleted - data is gone



**Solution: Volumes**

* Volumes stores data outside container
* Data survives even if container is removed.

Commands:

* Create volume: *docker volume create data\_volume*
* Use volume: *docker run -v data\_volume:/var/lib/MySQL MySQL*



**Blind Mount**

* Connects host folder to container: 

*docker run -v /data/MySQL:/var/lib/MySQL mysql*



**Storage Drivers**

Docker uses storage drivers to manage layers:

* Overlay2(most common)
* AUFS, BTRFS, Device Mapper etc

They decide how layers are stored are merged.























































































































































































































