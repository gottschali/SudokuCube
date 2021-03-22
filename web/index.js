import * as THREE from './three.module.js';
import {steps} from './steps.js'
// import {steps} from './baby_steps.js'
// Import the modules

// Orbit Controls
// Automatic resizing

// ------------------------------------------------
// BASIC SETUP
// ------------------------------------------------


// Create an empty scene
const scene = new THREE.Scene();

// Create a basic perspective camera
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );
camera.position.set(5, 5, 5);
camera.lookAt(new THREE.Vector3(0, 0, 0));

// Create a renderer with Antialiasing
const renderer = new THREE.WebGLRenderer({antialias:true});

// Configure renderer clear color
renderer.setClearColor("#2E2B40");

// Configure renderer size
renderer.setSize( window.innerWidth, window.innerHeight );

// Append Renderer to DOM
document.body.appendChild( renderer.domElement );

// ------------------------------------------------
// FUN STARTS HERE
// ------------------------------------------------

const diceGeometry = new THREE.BoxGeometry( 1, 1, 1 );

const material = new THREE.MeshBasicMaterial( { color: "#433F81" } );
const dice01 = new THREE.Mesh( diceGeometry, material );

const w_material = new THREE.MeshBasicMaterial( { color: "#00FF00",wireframe:true,transparent:true } );
const dice01_wireframe = new THREE.Mesh( diceGeometry, w_material );
dice01.add( dice01_wireframe );

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
let dices = {};
colors.forEach((c, i) => dices[i] = new THREE.Mesh(diceGeometry, new THREE.MeshBasicMaterial( {color: c})));

const cube = new THREE.Group();
cube.add( dice01 );
scene.add( cube );

// Render Loop
// var render = function () {
  // requestAnimationFrame( render );

  // dice01.x += 0.11;
  // dice01.y += 0.11;

  // Render the scene
  // renderer.render(scene, camera);
// };

function render(){
  // window.requestAnimationFrame( animation );

  cube.rotation.x = Date.now() * 0.00005;
  cube.rotation.y = Date.now() * 0.0001;
  // dice01.position.y += 0.0005;
  // dice01.position.z += 0.05;

  renderer.render( scene, camera);
}

const sleep = (milliseconds) => { return new Promise(resolve => setTimeout(resolve, milliseconds));};

function pause(millis)
{
    var date = new Date();
    var curDate = null;
    do { curDate = new Date(); }
    while(curDate-date < millis);
}

let history = [];

function move_cube(x, y, z, color) {
    const dice = dices[color - 1].clone();
    // var dice = new THREE.Mesh(diceGeometry, new THREE.MeshBasicMaterial( {color: colors[color]}));

	  history.push(dice)
    cube.add(dice);

	  dice.position.set(x, y, z);
    // render();
}


// Do lookup by name instead of hist array
//function removeEntity(object) {
    //var selectedObject = scene.getObjectByName(object.name);
    //scene.remove( selectedObject );
    //animate();
//}

function do_step(x, y, z, color) {
    if (color != 0) {
        move_cube(x, y, z, color);
    } else {
			// probably means remove
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

//steps.forEach(([[x, y, z], color]) => {
	//do_step(x, y, z, color);
	//render();
//});
// do_step(1, 0, 0, 1);
// do_step(-1, 1, 0, 2);

window.setInterval( run, 1 );


