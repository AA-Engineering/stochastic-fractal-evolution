# SFE-DC-001 — Constrained Thermal and Workload Evolution in Data Centers

**Status:** Proposed validation study. No efficiency advantage is claimed until benchmarked.

## Abstract

This study proposes applying Stochastic Fractal Evolution (SFE) to joint data-center workload placement and thermal/cooling control. The hypothesis is that SFE's multiscale stochastic histories, explicit constraint operator, rare transition classes, and ensemble-attractor analysis can provide anticipatory control under uncertain workload and thermal conditions. The study is designed to compare SFE against conventional reactive control, deterministic optimization, Monte Carlo/random-field forecasting, and modern thermal-aware workload/cooling methods.

## 1. Motivation and prior art

Data-center thermal management is already a mature research area. Published work shows that workload placement and cooling are coupled, and joint optimization can reduce cooling energy relative to treating them independently. Recent work also applies Markov processes, deep reinforcement learning, and integrated power-computing-cooling optimization. Therefore SFE cannot claim novelty merely for predicting temperatures or coordinating workload and cooling.

ASHRAE thermal guidance treats equipment inlet conditions as a central operational constraint. The 2021 guidance lists a recommended dry-bulb range of 18–27 °C for air-cooled A1–A4 classes under normal circumstances, while allowable ranges depend on equipment class. High-density H1 equipment has a narrower recommended temperature range. These ranges are engineering references, not universal SFE constants.

The SFE research question is narrower:

> Can an ensemble of recursively evolving, multiscale, constrained workload/thermal histories identify impending hotspots, inefficient operating regimes, or rare coupled failures early enough to improve energy/reliability tradeoffs relative to established baselines?

## 2. State vector

For a data center divided into racks/zones, define

```text
X_t = {
  T_in,t, T_out,t,
  P_IT,t, P_cool,t,
  W_t,
  F_t,
  L_t,
  C_t,
  R_t
}
```

where:

- `T_in`, `T_out`: rack/zone inlet and outlet temperatures;
- `P_IT`: IT electrical power;
- `P_cool`: cooling-system power;
- `W`: workload placement and queue state;
- `F`: airflow/flow state or reduced-order thermal field;
- `L`: utilization/load;
- `C`: cooling-control state;
- `R`: redundancy/equipment availability state.

## 3. SFE evolution

```text
K_t ~ P(K | X_t, H_t, E_t)
X~_(t+1) = Phi_Kt(X_t, H_t, E_t, epsilon_t)
X_(t+1) = C_DC[X~_(t+1)]
```

`H_t` stores relevant thermal/workload history, `E_t` represents external variables such as ambient conditions or electricity/carbon signals, and `epsilon_t` is a seeded stochastic field.

### Transition semantics

The original SFE 65/20/10/5 weights are **not** assumed for a data center. Transition probabilities must be learned or calibrated from workload/fault traces.

Candidate semantic classes:

- **continuity:** ordinary workload and thermal fluctuations;
- **mutation:** workload migration, local utilization burst, cooling-control shift;
- **major jump:** large AI/HPC load burst, cooling degradation, equipment outage, network bottleneck;
- **genesis/regime change:** sustained new workload mix, topology/redundancy change, or other operating regime transition.

## 4. Multiscale stochastic seed

Data-center demand is not independent white noise. SFE-DC should test correlated perturbations across:

- server;
- rack;
- aisle/zone;
- cluster;
- facility;
- seconds/minutes/hours.

A multiscale seed field `F_DC(x,t)` represents correlated workload/thermal susceptibility. This is a hypothesis to benchmark against simpler stochastic models, not an assertion that workload is intrinsically fractal.

## 5. Constraint operator

The data-center constraint operator should reject, project, or repair proposed states that violate modeled engineering limits:

```text
C_DC = {
  thermal operating envelope,
  server/rack electrical capacity,
  cooling capacity,
  airflow/thermal model,
  workload resource requirements,
  queue/deadline/SLA constraints,
  redundancy/availability constraints,
  actuator limits and rates
}
```

The study must document exactly how each constraint is enforced.

ASHRAE recommended/allowable envelopes may be used as reference constraints when appropriate to the simulated equipment class; manufacturer limits supersede generic assumptions for real hardware.

## 6. SFE thermal-attractor field

For rack or zone `i` and forecast horizon `tau`, define an ensemble hotspot frequency

```text
A_T(i,tau) =
  (1/N) sum_j I[T_i^(j)(t+tau) > T_limit]
```

This is an SFE model frequency, not automatically a calibrated real-world probability.

Other attractors may represent:

- high cooling-energy states;
- recirculation/hot-aisle failure patterns;
- SLA-risk states;
- repeated workload placements;
- combined thermal/electrical bottlenecks.

## 7. Control objective

A candidate multi-objective cost is

```text
J =
 w1 * E_IT
+ w2 * E_cooling
+ w3 * P_peak
+ w4 * thermal_violation_cost
+ w5 * SLA_violation_cost
+ w6 * migration_cost
+ w7 * reliability_risk
```

Weights must be declared before evaluation or included in a Pareto analysis.

SFE is not required to be the optimizer. A useful architecture may be:

```text
SFE future ensemble
        |
        v
risk/attractor estimates
        |
        v
established optimizer/controller
        |
        v
workload + cooling actions
```

This separation is important because SFE may prove more valuable as a future-state generator than as a replacement for established optimization/control algorithms.

## 8. Experimental design

### Phase A — synthetic known-answer thermal network

Construct a small RC thermal network with analytically/numerically verified dynamics.

Goal: ensure SFE reproduces the known temperature response when stochastic evolution is disabled.

Acceptance tests:

- transient temperature error;
- steady-state temperature error;
- energy-balance residual;
- exact seed reproducibility.

### Phase B — stochastic workload trace

Inject recorded or synthetic workload fluctuations while keeping the thermal plant fixed.

Compare:

1. persistence/reactive baseline;
2. deterministic model predictive control;
3. conventional Monte Carlo;
4. correlated random-field Monte Carlo;
5. SFE ensemble + same downstream controller.

Primary question: does SFE improve forecast distribution quality or hotspot warning without excessive computation?

### Phase C — rare fault injection

Blindly inject events such as:

- fan/cooling degradation;
- server outage;
- workload burst;
- airflow obstruction;
- sensor noise/failure.

Measure rare-event recall, false alarms, lead time, recovery energy, and SLA impact.

### Phase D — joint workload/cooling control

Use the same workload traces and physical plant for all methods.

Do not compare an SFE controller with a weak baseline only. Include a competitive thermal-aware optimization or learning-based baseline.

## 9. Primary metrics

### Energy

- total facility energy;
- IT energy;
- cooling energy;
- peak electrical demand;
- PUE where appropriate.

PUE should not be treated as the only objective because it does not by itself measure useful computational work or reliability.

### Thermal

- maximum inlet temperature;
- time outside selected recommended envelope;
- number/duration of thermal violations;
- hotspot forecast precision/recall;
- hotspot warning lead time.

### Computing

- throughput;
- latency;
- job completion time;
- SLA violations;
- workload migrations.

### Reliability/robustness

- constraint violations;
- fault recovery time;
- failure-risk proxy;
- performance under sensor/model error.

### Forecast quality

- CRPS or other distribution score;
- calibration;
- coverage of prediction intervals;
- rare-event Brier/log score;
- attractor stability across seeds.

### Computational burden

- simulation time;
- controller decision latency;
- number of model evaluations;
- memory/compute overhead.

## 10. Falsification criteria

SFE-DC should be considered unsupported or unnecessary if, after fair tuning:

- ordinary Monte Carlo/random-field models achieve equivalent distributional forecasts at lower cost;
- established MPC/DRL methods achieve equal or better energy/reliability performance without SFE forecasts;
- SFE attractors are unstable across seeds or parameter perturbations;
- apparent savings arise from violating thermal/SLA constraints;
- benefits disappear on unseen workload/fault traces.

Negative results should be published.

## 11. Candidate SFE advantages to test

These are hypotheses, not findings:

1. **Earlier hotspot detection** from an ensemble of correlated future histories.
2. **Better rare-event exploration** through explicit major-jump/regime transitions.
3. **Path dependence** through thermal/workload history.
4. **Auditable uncertainty** through preserved seeds and lineage.
5. **Attractor-based control** that identifies recurring inefficient operating states.
6. **Cross-scale modeling** linking server/rack/zone/facility perturbations.

## 12. Relationship to current research

Existing literature already demonstrates that thermal-aware workload placement, joint cooling/workload control, DRL, Markov modeling, and integrated power-computing-cooling optimization can improve data-center efficiency. SFE must therefore be evaluated as an additional stochastic future-generation/attractor layer, not presented as the invention of thermal-aware data-center control.

## 13. Proposed first benchmark

**SFE-DC-001A: Four-rack RC thermal network**

- four thermally coupled rack nodes;
- one cooling/supply node;
- bounded workload at each rack;
- known RC coefficients;
- fixed ambient/supply condition;
- deterministic reference solution;
- seeded multiscale workload perturbation;
- explicit inlet-temperature and capacity constraints.

Run at least 10,000 trajectories after deterministic verification.

Report:

1. deterministic-reference error;
2. forecast calibration;
3. hotspot prediction;
4. energy;
5. violations;
6. computational cost;
7. ablations removing multiscale correlation, history, jump classes, and attractor aggregation.

## 14. Publication rule

No statement that "SFE improves data-center efficiency" should be made until a preregistered or otherwise frozen benchmark demonstrates improvement on unseen traces relative to strong baselines.

## References

- ASHRAE Handbook, Data Centers and Telecommunications Facilities; Thermal Guidelines for Data Processing Environments, 5th ed. (2021).
- Gholipour et al. (2020), "Joint data center cooling and workload management: A thermal-aware approach," Future Generation Computer Systems 104, 174–186. DOI: 10.1016/j.future.2019.10.040.
- "A survey on data center cooling systems: Technology, power consumption modeling and control strategy optimization," Journal of Systems Architecture 119 (2021), 102253.
- "Exploring thermal management approaches in cloud computing environments," Next Energy 11 (2026), 100605.
- "Cross-sector management for workload scheduling and thermal environment in data centers," Energy 359 (2026), 141508.
- "Co-optimization of thermal-aware workload scheduling with deep reinforcement learning-based cooling control in data centers," Energy 344 (2026), 139965.
