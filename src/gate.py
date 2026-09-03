REQUIRED={'admission':['tenant_quota','regional_placement','burst_budget','priority','idempotency'],'fleet':['demand_forecast','warm_capacity','launch_latency','launch_success','bootstrap_success','drain','termination','orphan_detection','fallback_capacity'],'session':['state_machine','join_success','time_to_ready','media_health','reconnect','upload_retry','completion','customer_trace'],'media':['cpu_budget','memory_budget','bandwidth','scratch_space','backpressure','bounded_buffering','crash_isolation','graceful_shutdown'],'region':['latency','capacity','data_residency','egress_cost','failure_domain','provider_health'],'api':['auth','rate_limit','idempotency','timeout_budget','retry_semantics','webhook_guarantee','versioning','tenant_isolation','request_tracing'],'release':['immutable_image','integration_test','synthetic_meeting','canary_region','small_cohort','health_gate','rollback'],'observability':['fleet_metrics','session_metrics','api_metrics','cost_metrics','deployment_markers','alert_owner','runbook','customer_correlation'],'reliability':['blast_radius','scheduler_ha','queue_ha','storage_ha','provider_degradation','region_failover','incident_owner','postmortem'],'cost':['cost_per_session','cost_per_hour','idle_cost','failed_launch_cost','egress_cost','regional_variance','capacity_efficiency']}

def evaluate(spec):
    findings=[]
    for section, fields in REQUIRED.items():
        values=spec.get(section,{})
        for field in fields:
            if not values.get(field): findings.append(f'{section}.{field} is required')
    return {'allowed': not findings, 'findings': findings}
