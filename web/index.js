import * as THREE from './three.module.js';
// import {steps} from './steps.js'
import {steps} from './baby_steps.js'
// Import the modules

// Orbit Controls
// Automatic resizing

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );
camera.position.set(5, 5, 5);
camera.lookAt(new THREE.Vector3(0, 0, 0));
const renderer = new THREE.WebGLRenderer({antialias: true});
renderer.setClearColor("#2E2B40");
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );


const colors = [
    "#191716",
    "#E6AF2E",
    "#E0E2DB",
    "#3D348B",
    "#BEB7A4",
    "#EE6055",
    "#0D21A1",
    "#B27092",
    "#7C7287",
];
// Just use normal array
const makeDice = ( c => new THREE.Mesh(new THREE.BoxGeometry( 1, 1, 1 ), new THREE.MeshBasicMaterial( {color: c})));
let die = [];
colors.forEach( c => die.push( makeDice( c ) ));

const cube = new THREE.Group();
scene.add( cube );

function render(){
  cube.rotation.x = Date.now() * 0.00005;
  cube.rotation.y = Date.now() * 0.0001;

  renderer.render( scene, camera);
}


let history = [];

function move_cube(x, y, z, color) {
    const dice = die[color - 1].clone();
	  history.push(dice)
    cube.add(dice);
	  dice.position.set(x, y, z);
    // render();
}



function do_step(x, y, z, color) {
    if (color != 0) {
        move_cube(x, y, z, color);
    } else {
			// probably means remove
// Do lookup by name instead of hist array
			const dice = history.pop();
			cube.remove( dice );
        console.log("nothing");
    }
}
render();
let i = 0;
function run() {
	 if (i < steps.length)  {
      let [[x, y, z], color] = steps[i];
	    do_step(x, y, z, color);
	}
	 render();
	 i++;
}

window.setInterval( run, 1 );


