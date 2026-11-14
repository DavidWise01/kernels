/**
 * ECK-061: post-freeze cross-family transfer audit.
 * Run: node eck/test_eck061.cjs
 * Executes actual neural source and independent synthetic family evaluations.
 * Never opens the 145 original final-test examples.
 */
const assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const script=fs.readFileSync(path.join(__dirname,'index.html'),'utf8').split('<script>')[1].split('</script>')[0];
new Function(script);
const bounds=[
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
 ['const replicateSpec=','function replicateRender()'],
 ['const familySpec=','function familyRender()']
];
const sections=bounds.map(([a,b])=>{
 const i=script.indexOf(a),j=script.indexOf(b,i);
 assert.ok(i>=0&&j>i,'model section '+a);
 return script.slice(i,j);
});
const context=vm.createContext({});
vm.runInContext(sections.join('\n')+'\nfunction robustRender(){}\nfunction evidenceRender(){}\nfunction replicateRender(){}\nfunction familyRender(){}',context);
const report=vm.runInContext('familyAudit()',context);
assert.equal(report.passed,true);
assert.equal(report.modelsFrozen,true);
assert.equal(report.final,'WITHHELD');
assert.equal(report.spec.id,'ECK061_MOVING_BLOBS_CONTRAST_V1');
assert.deepEqual(Array.from(report.spec.taskSeeds),[101,211,307,401,503]);
assert.equal(report.rows.length,45);
for(const taskSeed of [101,211,307,401,503]){
 const rows=report.rows.filter(r=>r.taskSeed===taskSeed);
 assert.equal(rows.length,9);
 for(const row of rows){
  assert.ok(Number.isFinite(row.mse)&&row.mse>=0);
  assert.equal(row.existingFinal,'WITHHELD');
 }
}
assert.deepEqual(Array.from(report.winners),Array(5).fill('gradient'));
const values={
 fixed:{a:.0017331621120197664,b:.005279765937510281},
 ranked:{a:.0016793668390036906,b:.00527606000088156},
 gradient:{a:.00170319897554424,b:.005272647717112995}
};
for(const stat of report.stats){
 assert.ok(Math.abs(stat.familyA-values[stat.policy].a)<1e-12);
 assert.ok(Math.abs(stat.familyB-values[stat.policy].b)<1e-12);
 assert.ok(stat.familyB>stat.familyA);
 assert.ok(stat.acrossTasksSD>0);
}
const val=(p)=>report.stats.find(s=>s.policy===p);
assert.ok(val('ranked').familyA<val('gradient').familyA);
assert.ok(val('gradient').familyB<val('ranked').familyB);
assert.equal(vm.runInContext('familyProbe(101,0).planes.every(p=>p.every(v=>v>0&&v<1))',context),true);
assert.equal(vm.runInContext('tripleTrain.length',context),438);
assert.equal(vm.runInContext('tripleValid.length',context),146);
assert.equal(vm.runInContext('tripleTest.length',context),145);
assert.equal(vm.runInContext('dgState.final',context),null);
assert.equal(vm.runInContext('robustState.result.runs.every(r=>r.test==="WITHHELD")',context),true);
console.log('ECK-061 PASS: 45 new scores on spatial-blob family; 45 historical family A scores; 145 final sealed.');
console.log('Family B winner gradient on all five task averages; ranking flips vs family A.');
for(const stat of report.stats)console.log(stat.policy,'A',stat.familyA,'B',stat.familyB);
