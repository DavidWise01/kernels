/**
 * ECK-055: continuous safeguarded training vs fixed-rate, budget-accounted.
 * Run from repo root: node eck/test_eck055.cjs
 * No final-test model evaluation.
 */
const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const html=fs.readFileSync(path.join(__dirname,'index.html'),'utf8');
const source=html.split('<script>')[1].split('</script>')[0];
new Function(source);
const parts=[
 ['const spinorStages=','function iterateSpinorSlot()'],
 ['const neuralCarrierNames=','function renderNeuralCarriers()'],
 ['const tripleCases=','function drawTripleNet()'],
 ['const temporalState=','function renderTemporal()'],
 ['const adaptState=','function adaptRender()'],
 ['const forgeEdges=','function renderForge()'],
 ['const collisionState=','function collisionRender()'],
 ['const dgState=','function dgRender()'],
 ['const continuitySpec=','function continuityRender()']
].map(([a,b])=>{
 const i=source.indexOf(a),j=source.indexOf(b,i);
 assert.ok(i>=0&&j>i,a);
 return source.slice(i,j);
});
const context=vm.createContext({});
vm.runInContext(parts.join('\n')+'\nfunction continuityRender(){}',context);
const result=vm.runInContext('continuityExecute()',context);
assert.equal(result.passed,true);
assert.equal(result.spec.candidateBudget,40);
assert.equal(result.adaptive.proposals,22);
assert.equal(result.adaptive.accepted,7);
assert.equal(result.adaptive.rejected,15);
assert.equal(result.adaptive.stop,'NO_FEASIBLE_STEP');
assert.equal(result.fixed.proposals,40);
assert.equal(result.fixed.accepted,40);
assert.equal(result.fixed.rejected,0);
assert.equal(result.fixed.stop,'BUDGET_EXHAUSTED');
assert.ok(result.adaptive.final.validation<result.fixed.final.validation);
assert.ok(result.adaptive.final.repeated<result.fixed.final.repeated);
assert.ok(result.adaptive.final.distinct<result.fixed.final.distinct);
for(const model of [result.adaptive,result.fixed]){
 assert.equal(model.proposals,model.accepted+model.rejected);
 assert.equal(model.checkpoints.length,model.accepted+1);
 for(let i=1;i<model.checkpoints.length;i++){
  const before=model.checkpoints[i-1].metrics,after=model.checkpoints[i].metrics;
  assert.ok(after.train<before.train);
  assert.ok(after.validation<=before.validation+1e-12);
  assert.ok(after.repeated<=before.repeated+1e-12);
  assert.ok(after.distinct<=before.distinct+1e-12);
 }
 assert.equal(model.test,'WITHHELD');
 assert.equal(model.singlet,'(0=-.)');
}
assert.equal(vm.runInContext('tripleTrain.length',context),438);
assert.equal(vm.runInContext('tripleValid.length',context),146);
assert.equal(vm.runInContext('tripleTest.length',context),145);
assert.equal(vm.runInContext('dgState.final',context),null);
console.log('ECK-055 PASS: adaptive 7 accepts / 15 rejects / 22 proposals / bounded stop.');
console.log('Fixed 40 accepts / 0 rejects / 40 proposals.');
console.log('Validation MSE: adaptive',result.adaptive.final.validation,'fixed',result.fixed.final.validation);
console.log('Final 145 cases withheld.');
