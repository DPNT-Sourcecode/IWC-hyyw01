from __future__ import annotations

from .utils import call_dequeue, call_enqueue, call_size, iso_ts, run_queue


def test_enqueue_size_dequeue_flow() -> None:
    run_queue(
        [
            call_enqueue("companies_house", 1, iso_ts(delta_minutes=0)).expect(1),
            call_size().expect(1),
            call_dequeue().expect("companies_house", 1),
        ]
    )


def test_rule_of_three() -> None:
    run_queue(
        [
            call_enqueue(user_id=1, provider="companies_house", timestamp="2025-10-20 12:00:00").expect(1),
            call_enqueue(user_id=2, provider="bank_statements", timestamp="2025-10-20 12:00:00").expect(2),
            call_enqueue(user_id=1, provider="id_verification", timestamp="2025-10-20 12:00:00").expect(3),
            call_enqueue(user_id=1, provider="bank_statements", timestamp="2025-10-20 12:00:00").expect(4),
            call_size().expect(4),
            call_dequeue().expect("companies_house", 1),
            call_dequeue().expect("id_verification", 1),
            call_dequeue().expect("bank_statements", 1),
            call_dequeue().expect("bank_statements", 2),
        ]
    )


def test_timestamp_ordering() -> None:
    run_queue(
        [
            call_enqueue(user_id=1, provider="bank_statements", timestamp="2025-10-20 12:05:00").expect(1),
            call_enqueue(user_id=2, provider="bank_statements", timestamp="2025-10-20 12:00:00").expect(2),
            call_size().expect(2),
            call_dequeue().expect("bank_statements", 2),
            call_dequeue().expect("bank_statements", 1),
        ]
    )


def test_dependency_resolution() -> None:
    run_queue(
        [
            call_enqueue(user_id=1, provider="credit_check", timestamp="2025-10-20 12:00:00").expect(1),
            call_size().expect(2),
            call_dequeue().expect("bank_statements", 2),
            call_dequeue().expect("bank_statements", 1),
        ]
    )





