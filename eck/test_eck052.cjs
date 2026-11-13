/**
 * ECK-052: real-gradient adverse update witness, evaluated from eck/index.html.
 * Run from repository root: node eck/test_eck052.cjs
 *
 * Executes only model definitions (no DOM); does NOT open the 145-case final split.
 */
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const html = fs.readFileSync(require('node:path').join(__dirname,'index.html'),'utf8');
const script = html.split('<script>')[1].split('</script>')[0];
assert.ok(script, 'inline model script present');
new Function(script);
const bounds = [
 ['const spinorStages=', 'function iterateSpinorSlot()'],
 ['const neuralCarrierNames=', 'function renderNeuralCarriers()'],
 ['const tripleCases=', 'function drawTripleNet()'],
 ['const temporalState=', 'function renderTemporal()'],
 ['const adaptState=', 'function adaptRender()'],
 ['const forgeEdges=', 'function renderForge()'],
 ['const collisionState=', 'function collisionRender()'],
 ['const dgState=', 'function dgRender()']
];
const chunks = bounds.map(([start,end]) => {
 const left=script.indexOf(start),right=script.indexOf(end,left);
 assert.ok(left>=0 && right>left, 'found model block '+start);
 return script.slice(left,right);
});
const context=vm.createContext({});
vm.runInContext(chunks.join('\n')+'\nfunction dgRender(){}',context);
const witness=vm.runInContext('dgRealGradientWitness()',context);
assert.equal(witness.passes,true,'real gradient witness reproduces');
assert.equal(witness.warmup,20);
assert.equal(witness.challengeRate,70);
assert.equal(witness.ordinary,true,'ordinary learner accepts');
assert.equal(witness.strict,false,'dual-cohort learner rejects');
assert.equal(witness.source.version,20);
assert.equal(witness.ordinaryAcceptedVersion,21);
assert.equal(witness.protectedRetainedVersion,20);
assert.ok(witness.candidate.train < witness.previous.train);
assert.ok(witness.candidate.validation < witness.previous.validation);
assert.ok(witness.candidate.repeated < witness.previous.repeated);
assert.ok(witness.candidate.distinct > witness.previous.distinct);
assert.ok(Math.abs(witness.candidate.distinct - 0.0002342608367434893) < 1e-11);
assert.equal(vm.runInContext('tripleTrain.length',context),438);
assert.equal(vm.runInContext('tripleValid.length',context),146);
assert.equal(vm.runInContext('tripleTest.length',context),145);
assert.equal(vm.runInContext('dgState.final',context),null);
console.log('ECK-052 PASS: learned checkpoint 20; real-gradient rate 70; ordinary accepts, strict rejects.');
console.log('Train:',witness.previous.train,'->',witness.candidate.train);
console.log('Validation:',witness.previous.validation,'->',witness.candidate.validation);
console.log('Repeated:',witness.previous.repeated,'->',witness.candidate.repeated);
console.log('Distinct:',witness.previous.distinct,'->',witness.candidate.distinct);
console.log('Final-test partition: withheld.');
