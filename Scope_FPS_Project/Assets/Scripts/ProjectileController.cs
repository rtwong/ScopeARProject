using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class ProjectileController : MonoBehaviour {

    public AudioSource hit_sound;

	// Use this for initialization
	void Start () {
        hit_sound = GameObject.Find("Hit_sound").GetComponent<AudioSource>();
    }

    // Update is called once per frame
    void Update () {
	
	}

    void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.CompareTag("Target"))
        {
            GameManager.instance.count++;
            hit_sound.Play();
            Destroy(this.gameObject);
        }
    }


}
