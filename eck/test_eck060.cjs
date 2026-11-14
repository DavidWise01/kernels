/**
 * ECK-060 — reproducible five-task post-freeze transfer evaluation.
 * Run: node eck/test_eck060.cjs
 * Reads source neural modules and evaluates 45 task/model combinations;
 * no original final-test predictions are made.
 */
const assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const source=fs.readFileSync(path.join(__dirname,'index.html'),'utf8').split('<script>')[1].split('</script>')[0];
new Function(source);
const ranges=[
 ['const spinorStages=','function iterateSpinorSlot()'],
 ['const neuralCarrierNames=','function renderNeuralCarriers()'],
 ['const tripleCases=','function drawTripleNet()'],
 ['const temporalState=','function renderTemporal()'],
 ['const adaptState=','function adaptRender()'],
 ['const forgeEdges=','function renderForge()'],
 ['const nState=','function nRender()'],
 ['const shiftState=','function shiftRender()'],
 ['const seedLab=','function renderSeedLab()'],
 ['const collisionState=','function collisionRender()'],
 ['const dgState=','function dgRender()'],
 ['const rankSpec=','function rankRender()'],
 ['const robustSpec=','function robustRender()'],
 ['const evidenceProtocol=','function evidenceRender()'],
 ['const replicateSpec=','function replicateRender()']
];
const chunks=ranges.map(([a,b])=>{
 const i=source.indexOf(a),j=source.indexOf(b,i);
 assert.ok(i>=0&&j>i,'missing '+a);
 return source.slice(i,j);
});
const context=vm.createContext({});
vm.runInContext(chunks.join('\n')+'\nfunction robustRender(){}\nfunction evidenceRender(){}\nfunction replicateRender(){}',context);
const result=vm.runInContext('replicateAudit()',context);
assert.equal(result.passed,true);
assert.equal(result.modelsFrozen,true);
assert.equal(result.rows.length,45);
assert.equal(result.final,'WITHHELD');
assert.equal(result.spec.id,'ECK060_REPLICATED_CONTINUOUS_TRANSFER_V1');
assert.equal(result.spec.probesPerTask,81);
assert.deepEqual(Array.from(result.spec.taskSeeds),[11,23,37,53,71]);
assert.deepEqual(Array.from(result.spec.modelSeeds),[0,1,2]);
assert.deepEqual(Array.from(result.spec.policies),['fixed','ranked','gradient']);
for(const taskSeed of [11,23,37,53,71]){
 assert.equal(result.rows.filter(r=>r.taskSeed===taskSeed).length,9);
 for(const modelSeed of [0,1,2]){
  for(const policy of ['fixed','ranked','gradient']){
   const row=result.rows.find(r=>r.taskSeed===taskSeed&&r.modelSeed===modelSeed&&r.policy===policy);
   assert.ok(row);
   assert.equal(row.trainedBeforeEvaluation,true);
   assert.equal(row.final,'WITHHELD');
   assert.equal(row.candidates,40);
   assert.ok(Number.isFinite(row.score));
   assert.ok(row.score>=0);
  }
 }
}
const expected={
 fixed:0.0017331621120197664,
 ranked:0.0016793668390036906,
 gradient:0.00170319897554424
};
for(const entry of result.policyStats){
 assert.ok(Math.abs(entry.mean-expected[entry.policy])<1e-12);
 assert.equal(entry.taskMeans.length,5);
 assert.equal(entry.modelMeans.length,3);
 assert.ok(entry.acrossTasksSD>entry.acrossModelStartsSD);
}
assert.deepEqual(Array.from(result.taskWinners),['ranked','ranked','ranked','ranked','ranked']);
assert.ok(result.paired.every(r=>r.rankedMinusFixed<0&&r.gradientMinusFixed<0));
assert.equal(vm.runInContext('replicateProbe(11,0).planes.every(p=>p.every(x=>x>0&&x<1))',context),true);
assert.equal(vm.runInContext('tripleTrain.length',context),438);
assert.equal(vm.runInContext('tripleValid.length',context),146);
assert.equal(vm.runInContext('tripleTest.length',context),145);
assert.equal(vm.runInContext('dgState.final',context),null);
assert.equal(vm.runInContext('robustState.result.runs.every(r=>r.test==="WITHHELD")',context),true);
console.log('ECK-060 PASS: 5 new synthetic task seeds × 9 frozen model configurations = 45 scores.');
for(const s of result.policyStats){
 console.log(s.policy,'mean',s.mean,'acrossTasksSD',s.acrossTasksSD,'acrossModelStartsSD',s.acrossModelStartsSD);
}
console.log('Original 145-case final partition WITHHELD.');
