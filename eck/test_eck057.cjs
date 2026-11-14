/**
 * ECK-057 — evidence-ranked vs fixed-order carrier-block selection.
 * Run: node eck/test_eck057.cjs
 * Extracts neural model from index.html; final-test cases never evaluated.
 */
const assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const html=fs.readFileSync(path.join(__dirname,'index.html'),'utf8');
const source=html.split('<script>')[1].split('</script>')[0];
assert.ok(source);
new Function(source);
const bounds=[
 ['const spinorStages=','function iterateSpinorSlot()'],
 ['const neuralCarrierNames=','function renderNeuralCarriers()'],
 ['const tripleCases=','function drawTripleNet()'],
 ['const temporalState=','function renderTemporal()'],
 ['const adaptState=','function adaptRender()'],
 ['const forgeEdges=','function renderForge()'],
 ['const collisionState=','function collisionRender()'],
 ['const dgState=','function dgRender()'],
 ['const rankSpec=','function rankRender()']
];
const chunks=bounds.map(([a,b])=>{
 const i=source.indexOf(a),j=source.indexOf(b,i);
 assert.ok(i>=0&&j>i,a);
 return source.slice(i,j);
});
const context=vm.createContext({});
vm.runInContext(chunks.join('\n')+'\nfunction rankRender(){}',context);
const r=vm.runInContext('rankCompare()',context);
assert.equal(r.passed,true);
assert.equal(r.fixed.cost,40);
assert.equal(r.ranked.cost,40);
assert.equal(r.fixed.accepted,13);
assert.equal(r.ranked.accepted,17);
assert.equal(r.fixed.stalls.length,2);
assert.equal(r.ranked.stalls.length,1);
assert.equal(r.fixed.selections[0].block,'weak');
assert.equal(r.ranked.selections[0].block,'fusion');
assert.equal(r.fixed.selections[0].probes,1);
assert.equal(r.ranked.selections[0].probes,5);
assert.equal(r.ranked.selections[0].from,7);
assert.equal(r.ranked.selections[0].to,8);
const probes=r.ranked.attempts.filter(x=>x.kind==='block');
assert.deepEqual(Array.from(probes,x=>x.block),['weak','medium','strong','fusion','repair']);
assert.deepEqual(Array.from(probes,x=>x.accepted),[true,false,false,true,false]);
const best=probes.filter(x=>x.accepted).sort((a,b)=>b.improvement-a.improvement)[0];
assert.equal(best.block,'fusion');
assert.ok(best.improvement>probes[0].improvement);
assert.ok(Math.abs(r.ranked.final.validation-0.00002260419077305051)<1e-12);
assert.ok(Math.abs(r.fixed.final.validation-0.00003777177241941231)<1e-12);
for(const policy of [r.fixed,r.ranked]){
 assert.equal(policy.test,'WITHHELD');
 assert.equal(policy.singlet,'(0=-.)');
 assert.equal(policy.checkpoints.length,policy.accepted+1);
 for(let i=1;i<policy.checkpoints.length;i++){
  const a=policy.checkpoints[i-1].metrics,b=policy.checkpoints[i].metrics;
  assert.ok(b.train<a.train);
  assert.ok(b.validation<=a.validation+1e-12);
  assert.ok(b.repeated<=a.repeated+1e-12);
  assert.ok(b.distinct<=a.distinct+1e-12);
 }
}
assert.equal(vm.runInContext('tripleTrain.length',context),438);
assert.equal(vm.runInContext('tripleValid.length',context),146);
assert.equal(vm.runInContext('tripleTest.length',context),145);
console.log('ECK-057 PASS: fixed 13 checkpoints / ranked 17; both 40 gradient candidates.');
console.log('Ranked chose Fusion after five measured block probes.');
console.log('Validation:',r.fixed.final.validation,'->',r.ranked.final.validation);
console.log('Final 145 cases withheld.');
