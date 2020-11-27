import * as THREE from 'https://threejsfundamentals.org/threejs/resources/threejs/r122/build/three.module.js';
import {TrackballControls} from 'https://threejsfundamentals.org/threejs/resources/threejs/r122/examples/jsm/controls/TrackballControls.js';
import {OrbitControls} from 'https://threejsfundamentals.org/threejs/resources/threejs/r122/examples/jsm/controls/OrbitControls.js';


import {OBJLoader2} from 'https://threejsfundamentals.org/threejs/resources/threejs/r122/examples/jsm/loaders/OBJLoader2.js';

    function loadObj() {
        const canvas = document.querySelector('#c');
        const renderer = new THREE.WebGLRenderer({
            canvas,
            alpha: true,
        });
        const fov = 65;
        const aspect = 2;
        const near = 0.1;
        const far = 1000;
        const camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
        camera.position.set(-20, -180, 110);

        const controls = new TrackballControls(camera, canvas);
        controls.target.set(0, 0, 0);

        const scene = new THREE.Scene();

        {
            const skyColor = 0xB1E1FF;
            const groundColor = 0xB97A20;
            const intensity = 1;
            const light = new THREE.HemisphereLight(skyColor, groundColor, intensity);
            scene.add(light);
        }

        {
            const color = 0xFFFFFF;
            const intensity = 1;
            const light = new THREE.DirectionalLight(color, intensity);
            light.position.set(0, 10, 0);
            light.target.position.set(-5, 0, 0);
            scene.add(light);
            scene.add(light.target);
        }

        {
            const objLoader = new OBJLoader2();
            objLoader.load("threejs/house_sample.obj", (root) => {
            //scene.add(root);
                var box = new THREE.Box3().setFromObject( root );
                box.getCenter( root.position );
                root.position.multiplyScalar( - 1 );

                var pivot = new THREE.Group();
                scene.add( pivot );
                pivot.add( root );
            });
        }

        function resizeRendererToDisplaySize(renderer) {
            const canvas = renderer.domElement;
            const width = canvas.clientWidth;
            const height = canvas.clientHeight;
            const needResize = canvas.width !== width || canvas.height !== height;
            if (needResize) {
                renderer.setSize(width*4, height*4, false);
            }
            return needResize;
        }

        function render() {

            if (resizeRendererToDisplaySize(renderer)) {
                const canvas = renderer.domElement;
                camera.aspect = canvas.clientWidth / canvas.clientHeight;
                camera.updateProjectionMatrix();
            }

            renderer.setSize(1200, 800);
            renderer.render(scene, camera);
            controls.update();
            requestAnimationFrame(render);
        }

        requestAnimationFrame(render);
    }

    loadObj();