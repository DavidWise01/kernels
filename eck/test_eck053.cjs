/**
 * ECK-053 — real model-derived constrained step recovery regression.
 * Run: node eck/test_eck053.cjs
 * Reads eck/index.html, executes only neural definitions, never evaluates final tests.
 */
const fs=require('node:fs');
const vm=require('node:vm');
const path=require('node:path');
const assert=require('node:assert/strict');
const html=fs.readFileSync(path.join(__dirname,'index.html'),'utf8');
const script=html.split('<script>')[1].split('</script>')[0];
assert.ok(script);
new Function(script);
const bounds=[
 ['const spinorStages=','function iterateSpinorSlot()'],
 ['const neuralCarrierNames=','function renderNeuralCarriers()'],
 ['const tripleCases=','function drawTripleNet()'],
 ['const temporalState=','function renderTemporal()'],
 ['const adaptState=','function adaptRender()'],
 ['const forgeEdges=','function renderForge()'],
 ['const collisionState=','function collisionRender()'],
 ['const dgState=','function dgRender()']
];
const pieces=bounds.map(([a,b])=>{
 const start=script.indexOf(a),end=script.indexOf(b,start);
 assert.ok(start>=0&&end>start,a);
 return script.slice(start,end);
});
const context=vm.createContext({});
vm.runInContext(pieces.join('\n')+'\nfunction dgRender(){}',context);
const result=vm.runInContext('dgRecoverSafeStep()',context);
assert.equal(result.passed,true);
assert.equal(result.source.version,20);
assert.equal(result.rejected.rate,70);
assert.equal(result.rejected.ordinary,true);
assert.equal(result.rejected.accepted,false);
assert.equal(result.winner.rate,60);
assert.equal(result.winner.version,21);
assert.equal(result.declaredRates.length,21);
assert.equal(result.trials.length,21);
assert.equal(result.trials.filter(x=>x.accepted).length,20);
assert.ok(result.winner.train<result.source.train);
assert.ok(result.winner.validation<result.source.validation);
assert.ok(result.winner.repeated<result.source.repeated);
assert.ok(result.winner.distinct<result.source.distinct);
assert.ok(Math.abs(result.winner.validation-0.000222340099972736)<1e-12);
assert.ok(Math.abs(result.winner.distinct-0.000151599535235541)<1e-12);
assert.equal(result.singlet,'(0=-.)');
assert.equal(result.finalTest,'WITHHELD');
assert.equal(vm.runInContext('tripleTrain.length',context),438);
assert.equal(vm.runInContext('tripleValid.length',context),146);
assert.equal(vm.runInContext('tripleTest.length',context),145);
assert.equal(vm.runInContext('dgState.final',context),null);
console.log('ECK-053 PASS: 21 rates, 70 rejected, 60 recovered; version 20 -> 21.');
console.log('Train / validation / repeated / distinct:',result.winner.train,result.winner.validation,result.winner.repeated,result.winner.distinct);
console.log('Final-test partition: WITHHELD');
